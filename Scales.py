from typing import Type

import Notes
import Chords


class Scale:
    def __init__(self):
        self.keynote: Type[Notes.Note]
        self.notes: list[Type[Notes.Note]] = []

    def contains(self, note: Notes.Note | Type[Notes.Note]) -> bool:
        if isinstance(note, Notes.Note):
            return any(map(lambda x: isinstance(note, x), self.notes))
        else:
            return any(map(lambda x: note == x, self.notes))

    def count_hits(self, notes: list[Notes.Note]):
        return sum(map(self.contains, notes))

    def get_parallel_scale(self):
        return None


class MajorScale(Scale):
    scheme = [0, 2, 4, 5, 7, 9, 11]
    applicable_chords = [Chords.MajorChord, Chords.MinorChord, Chords.MinorChord, Chords.MajorChord,
                         Chords.MajorChord, Chords.MinorChord, Chords.DiminishedChord]

    def __init__(self, keynote: Notes.Note | Type[Notes.Note]):
        super(MajorScale, self).__init__()
        if isinstance(keynote, Notes.Note):
            self.keynote = keynote.__class__
        else:
            self.keynote = keynote
        keynote_index = Notes.notes_list.index(self.keynote)
        current_scheme = [(index + keynote_index) % len(Notes.notes_list) for index in self.scheme]

        self.notes = [Notes.notes_list[index] for index in current_scheme]

    def get_parallel_scale(self):
        return MinorScale(
            Notes.notes_list[(self.scheme[-2] + Notes.notes_list.index(self.keynote)) % len(Notes.notes_list)]
        )


class MinorScale(Scale):
    scheme = [0, 2, 3, 5, 7, 8, 10]
    applicable_chords = [Chords.MinorChord, Chords.DiminishedChord, Chords.MajorChord, Chords.MinorChord,
                         Chords.MinorChord, Chords.MajorChord, Chords.MajorChord]

    def __init__(self, keynote: Notes.Note | Type[Notes.Note]):
        super(MinorScale, self).__init__()
        if isinstance(keynote, Notes.Note):
            self.keynote = keynote.__class__
        else:
            self.keynote = keynote
        keynote_index = Notes.notes_list.index(self.keynote)
        current_scheme = [(index + keynote_index) % len(Notes.notes_list) for index in self.scheme]

        self.notes = [Notes.notes_list[index] for index in current_scheme]

    def get_parallel_scale(self):
        return MajorScale(
            Notes.notes_list[(self.scheme[2] + Notes.notes_list.index(self.keynote)) % len(Notes.notes_list)]
        )
