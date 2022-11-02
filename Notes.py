from typing import Type


class Note:
    def __init__(self, note: int):
        self.octave = note // 12

    def __repr__(self):
        return f'Note {self.__class__.__name__.replace("Sharp", "#")} of {self.octave}th octave'

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.octave == self.octave

    def __hash__(self):
        return hash(f'{self.__class__}{self.octave}')

    @classmethod
    def get_note_from_height(cls, note: int):
        note_types = [C, CSharp, D, DSharp, E, F, FSharp, G, GSharp, A, ASharp, B]
        return note_types[note % 12](note)


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


class Rest(Note):
    def __init__(self):
        super(Rest, self).__init__(0)


notes_list = [C, CSharp, D, DSharp, E, F, FSharp, G, GSharp, A, ASharp, B]
major_scheme = [0, 2, 4, 5, 7, 9, 11]
minor_scheme = [0, 2, 3, 5, 7, 8, 10]


def get_major_scale(keynote_cls: Type[Note]) -> list[Type[Note]]:
    keynote_index = notes_list.index(keynote_cls)
    scheme = [(index + keynote_index) % len(notes_list) for index in major_scheme]
    return [notes_list[index] for index in scheme]


def get_minor_scale(keynote_cls: Type[Note]) -> list[Type[Note]]:
    keynote_index = notes_list.index(keynote_cls)
    scheme = [(index + keynote_index) % len(notes_list) for index in minor_scheme]
    return [notes_list[index] for index in scheme]


def get_parallel_minor_tonic(keynote_cls: Type[Note]) -> Type[Note]:
    return notes_list[(major_scheme[5] + notes_list.index(keynote_cls)) % len(notes_list)]


def get_parallel_major_tonic(keynote_cls: Type[Note]) -> Type[Note]:
    return notes_list[(minor_scheme[2] + notes_list.index(keynote_cls)) % len(notes_list)]
