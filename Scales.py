from typing import Type
from operator import itemgetter
import abc

import Notes
import Chords


class Scale:
    __metaclass__ = abc.ABCMeta
    scheme: list[int]
    applicable_chords: list[Type[Chords.Chord]]

    def __init__(self, keynote: Type[Notes.Note]):
        self.keynote: Type[Notes.Note]
        self.notes: list[Type[Notes.Note]] = []

        self.keynote = keynote
        self.notes = [keynote.get_next(interval) for interval in self.scheme]

    def __repr__(self):
        return f'{self.keynote.__name__} {self.__class__.__name__}'

    def contains(self, note: Type[Notes.Note]) -> bool:
        return any(map(lambda x: note == x, self.notes))

    def count_hits(self, notes: list[Type[Notes.Note]]) -> int:
        return sum(map(self.contains, notes))

    def get_chord_from(self, degree: int):
        chord_type = self.applicable_chords[degree]
        chord_keynote = self.keynote.get_next(self.scheme[degree])
        return chord_type(chord_keynote)

    @abc.abstractmethod
    def get_parallel_scale(self):
        return

    @staticmethod
    def get_most_probable_scales(track_notes: list[Type[Notes.Note]], sample_size: int = 4) -> list:
        notes_list = Notes.Note.get_notes_list()
        major_scales = [MajorScale(note) for note in notes_list]
        hits = [scale.count_hits(track_notes) for scale in major_scales]
        hits_of_major_scales_sorted = list(sorted(zip(hits, major_scales), key=itemgetter(0), reverse=True))
        major_scales_sorted = list(map(itemgetter(1), hits_of_major_scales_sorted))
        sampled_major_scales = major_scales_sorted[:len(major_scales_sorted) // sample_size]
        sampled_scales = [*sampled_major_scales, *[scale.get_parallel_scale() for scale in sampled_major_scales]]
        return sampled_scales


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

    def get_parallel_scale(self) -> MajorScale:
        return MajorScale(self.keynote.get_next(self.scheme[2]))
