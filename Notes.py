class Note:
    def __init__(self, height: int, start_time: int, finish_time: int):
        self.height = height
        self.start_time = start_time
        self.finish_time = finish_time
        self.octave = height // 12

    def __repr__(self):
        return f'Note {self.__class__.__name__.replace("Sharp", "#")} of {self.octave}th octave'

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.octave == self.octave

    def __hash__(self):
        return hash(f'{self.__class__}{self.octave}')

    @classmethod
    def get_note_key(cls, octave) -> int:
        notes_list = Note.__subclasses__()
        return octave * 12 + notes_list.index(cls)

    @classmethod
    def get_notes_list(cls):
        return cls.__subclasses__()

    @classmethod
    def get_note_from_height(cls, note: int, start_time: int, finish_time: int):
        notes_list = cls.__subclasses__()
        return notes_list[note % len(notes_list)](note, start_time, finish_time)

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
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(C, self).__init__(height, start_time, finish_time)


class CSharp(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(CSharp, self).__init__(height, start_time, finish_time)


class D(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(D, self).__init__(height, start_time, finish_time)


class DSharp(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(DSharp, self).__init__(height, start_time, finish_time)


class E(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(E, self).__init__(height, start_time, finish_time)


class F(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(F, self).__init__(height, start_time, finish_time)


class FSharp(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(FSharp, self).__init__(height, start_time, finish_time)


class G(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(G, self).__init__(height, start_time, finish_time)


class GSharp(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(GSharp, self).__init__(height, start_time, finish_time)


class A(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(A, self).__init__(height, start_time, finish_time)


class ASharp(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(ASharp, self).__init__(height, start_time, finish_time)


class B(Note):
    def __init__(self, height: int, start_time: int, finish_time: int):
        super(B, self).__init__(height, start_time, finish_time)
