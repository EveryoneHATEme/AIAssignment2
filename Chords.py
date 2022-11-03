from typing import Type

import Notes


class Chord:
    scheme: tuple[int]

    def __init__(self, keynote: Type[Notes.Note]):
        self.notes: list[Type[Notes.Note]]

        self.notes = [keynote.get_next(interval) for interval in self.scheme]

    def __repr__(self):
        return f'{self.__class__.__name__} of notes {", ".join([note.__name__ for note in self.notes])}'

    def __iter__(self):
        return iter(self.notes)


class MajorChord(Chord):
    scheme = (0, 4, 7)


class MinorChord(Chord):
    scheme = (0, 3, 7)


class DiminishedChord(Chord):
    scheme = (0, 3, 6)


class SuspendedSecondChord(Chord):
    scheme = (0, 2, 7)


class SuspendedFourthChord(Chord):
    scheme = (0, 5, 7)
