from operator import attrgetter
import mido

import Notes
import Scales
from TimeSignature import TimeSignature


class Track:
    def __init__(self, track: mido.MidiTrack, time_signature: TimeSignature, ticks_per_beat: int):
        self.notes: list[Notes.Note] = list()
        self.time_signature = TimeSignature(*time_signature)
        self.ticks_per_beat = ticks_per_beat * 2
        self.total_time = 0
        self._parse_track(track)
        self.most_probable_scales = Scales.Scale.get_most_probable_scales(
            list(map(attrgetter('__class__'), self.notes))
        )

    def get_beats_count(self):
        beats_amount = self.total_time // self.ticks_per_beat
        additional_beat = self.total_time % self.ticks_per_beat != 0
        return beats_amount + (1 if additional_beat else 0)

    def get_beats(self) -> list[list[Notes.Note]]:
        beats: list[list[Notes.Note]] = [[] for _ in range(self.get_beats_count())]

        for note in self.notes:
            # beat index on which the note starts to play
            start_beat_index = note.start_time // self.ticks_per_beat
            # beat index on which the note finishes playing
            finish_beat_index = (note.finish_time - 1) // self.ticks_per_beat

            beats[start_beat_index].append(note)

            if start_beat_index != finish_beat_index:
                beats[finish_beat_index].append(note)

        return beats

    def _parse_track(self, track: mido.MidiTrack) -> None:
        playing_notes: dict[int, list[Notes.Note]] = dict()

        for message in track:
            if isinstance(message, mido.MetaMessage):
                continue

            self.total_time += message.time

            match message.type:
                case 'note_on':
                    note = Notes.Note.get_note_from_height(message.note, self.total_time, 0)
                    if message.note in playing_notes:
                        playing_notes[message.note].append(note)
                    else:
                        playing_notes[message.note] = [note]
                case 'note_off':
                    note = playing_notes[message.note].pop()
                    note.finish_time = self.total_time
                    self.notes.append(note)
