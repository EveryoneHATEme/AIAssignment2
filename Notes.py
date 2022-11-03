from typing import Type


class Note:
    def __init__(self, note: int):
        self.octave = note // 12

    @staticmethod
    def create_from_octave(octave: int):
        return Note(octave * 12)

    def __repr__(self):
        return f'Note {self.__class__.__name__.replace("Sharp", "#")} of {self.octave}th octave'

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.octave == self.octave

    def __hash__(self):
        return hash(f'{self.__class__}{self.octave}')

    @classmethod
    def get_notes_list(cls):
        return cls.__subclasses__()

    @classmethod
    def get_note_from_height(cls, note: int):
        notes_list = cls.__subclasses__()
        return notes_list[note % len(notes_list)](note)

    @staticmethod
    def get_interval(first, second):
        notes_list = Note.__subclasses__()
        first_index = notes_list.index(first)
        second_index = notes_list.index(second)
        return abs(first_index - second_index)

    @classmethod
    def get_next(cls, interval: int):
        notes_list = Note.__subclasses__()
        note_index = notes_list.index(cls)
        return notes_list[(note_index + interval) % len(notes_list)]


class C(Note):
    def __init__(self, note: int):
        super(C, self).__init__(note)


class CSharp(Note):
    def __init__(self, note: int):
        super(CSharp, self).__init__(note)


class D(Note):
    def __init__(self, note: int):
        super(D, self).__init__(note)


class DSharp(Note):
    def __init__(self, note: int):
        super(DSharp, self).__init__(note)


class E(Note):
    def __init__(self, note: int):
        super(E, self).__init__(note)


class F(Note):
    def __init__(self, note: int):
        super(F, self).__init__(note)


class FSharp(Note):
    def __init__(self, note: int):
        super(FSharp, self).__init__(note)


class G(Note):
    def __init__(self, note: int):
        super(G, self).__init__(note)


class GSharp(Note):
    def __init__(self, note: int):
        super(GSharp, self).__init__(note)


class A(Note):
    def __init__(self, note: int):
        super(A, self).__init__(note)


class ASharp(Note):
    def __init__(self, note: int):
        super(ASharp, self).__init__(note)


class B(Note):
    def __init__(self, note: int):
        super(B, self).__init__(note)
