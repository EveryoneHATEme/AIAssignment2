from typing import Type
from operator import itemgetter

import Notes
import Chords


class Scale:
    scheme: list[int]
    applicable_chords: list[Type[Notes.Note]]

    def __init__(self, keynote: Type[Notes.Note]):
        self.keynote: Type[Notes.Note]
        self.notes: list[Type[Notes.Note]] = []

        self.keynote = keynote
        self.notes = [keynote.get_next(interval) for interval in self.scheme]

    def contains(self, note: Notes.Note | Type[Notes.Note]) -> bool:
        if isinstance(note, Notes.Note):
            return any(map(lambda x: isinstance(note, x), self.notes))
        else:
            return any(map(lambda x: note == x, self.notes))

    def count_hits(self, notes: list[Notes.Note]):
        return sum(map(self.contains, notes))

    def get_parallel_scale(self):
        return None

    @staticmethod
    def get_most_probable_scales(track_notes: list[Type[Notes]], sample_size=4):
        notes_list = Notes.Note.get_notes_list()
        major_scales = [MajorScale(note) for note in notes_list]
        hits = [scale.count_hits(track_notes) for scale in major_scales]
        major_scales_hits_sorted = list(sorted(zip(major_scales, hits), key=itemgetter(1)))


class MajorScale(Scale):
    scheme = [0, 2, 4, 5, 7, 9, 11]
    applicable_chords = [Chords.MajorChord, Chords.MinorChord, Chords.MinorChord, Chords.MajorChord,
                         Chords.MajorChord, Chords.MinorChord, Chords.DiminishedChord]

    def get_parallel_scale(self):
        return MinorScale(self.keynote.get_next(self.scheme[5]))


class MinorScale(Scale):
    scheme = [0, 2, 3, 5, 7, 8, 10]
    applicable_chords = [Chords.MinorChord, Chords.DiminishedChord, Chords.MajorChord, Chords.MinorChord,
                         Chords.MinorChord, Chords.MajorChord, Chords.MajorChord]

    def get_parallel_scale(self):
        return MinorScale(self.keynote.get_next(self.scheme[2]))
