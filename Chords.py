from typing import Type

import Notes


class Chord:
    scheme: tuple[int]

    def __init__(self, keynote: Type[Notes.Note]):
        self.notes: list[Type[Notes.Note]]

        keynote_index = Notes.notes_list.index(keynote)
        current_scheme = [(keynote_index + i) % len(Notes.notes_list) for i in self.scheme]
        self.notes = [Notes.notes_list[i] for i in current_scheme]

    def __repr__(self):
        return f'{self.__class__.__name__} of notes {", ".join([note.__name__ for note in self.notes])}'


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
