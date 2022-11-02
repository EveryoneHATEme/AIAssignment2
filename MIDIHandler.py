import mido


class MIDIHandler:
    def __init__(self, filename):
        self.file = mido.MidiFile(filename)
