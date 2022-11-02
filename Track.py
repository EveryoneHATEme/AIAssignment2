import mido

import Notes
import Scales
from NoteTimeStamped import NoteTimeStamped
from TimeSignature import TimeSignature


class Track:
    def __init__(self, track: mido.MidiTrack, time_signature: TimeSignature, ticks_per_beat: int):
        self.notes_stamped: list[NoteTimeStamped] = list()
        self.time_signature = TimeSignature(*time_signature)
        self.ticks_per_beat = ticks_per_beat * self.time_signature.numerator
        self.total_time = 0
        self._parse_track(track)

    def get_beats(self) -> list[list[NoteTimeStamped]]:
        beats_amount = self.total_time // self.ticks_per_beat
        additional_beat = self.total_time % self.ticks_per_beat != 0
        beats: list[list[NoteTimeStamped]] = [[] for _ in range(beats_amount + (1 if additional_beat else 0))]

        for note in self.notes_stamped:
            # beat index on which the note starts to play
            start_beat_index = note.start_time // self.ticks_per_beat
            # beat index on which the note finishes playing
            finish_beat_index = (note.finish_time - 1) // self.ticks_per_beat

            beats[start_beat_index].append(note)

            if start_beat_index != finish_beat_index:
                beats[finish_beat_index].append(note)

        return beats

    def get_notes(self) -> list[Notes.Note]:
        return [note_stamped.note for note_stamped in self.notes_stamped]

    def find_major_keynote(self):
        notes_list = self.get_notes()
        scales = [Scales.MajorScale(keynote) for keynote in Notes.notes_list]
        hits = [scale.count_hits(notes_list) for scale in scales]
        print(hits)

    def _parse_track(self, track: mido.MidiTrack) -> None:
        playing_notes: dict[int, list[NoteTimeStamped]] = dict()

        for message in track:
            if isinstance(message, mido.MetaMessage):
                continue

            self.total_time += message.time

            if message.type == 'note_on':
                note_time_stamped = NoteTimeStamped(Notes.Note.get_note_from_height(message.note), self.total_time)
                if message.note in playing_notes:
                    playing_notes[message.note].append(note_time_stamped)
                else:
                    playing_notes[message.note] = [note_time_stamped]
            elif message.type == 'note_off':
                current_note = playing_notes[message.note].pop()
                note_time_stamped = NoteTimeStamped(current_note.note, current_note.start_time, self.total_time)
                self.notes_stamped.append(note_time_stamped)
