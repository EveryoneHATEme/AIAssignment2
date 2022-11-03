import Notes
from Track import Track
from Chords import Chord


class GeneticAlgorithm:
    rewards = [
        300,    # perfect unison
        -300,   # minor second
        -100,   # major second
        0,      # minor third
        100,    # major third
        200,    # perfect fourth
        -200,   # augmented fourth / diminished fifth
        200,    # perfect fifth
        100,    # minor sixth
        0,      # major sixth
        -100,   # minor seventh
        -300,   # major seventh
    ]

    def __init__(self, track: Track):
        self.track = track

    def fitness(self, chord: Chord, beat: list[Notes.Note]):
        result = 0

        for beat_note in beat:
            for chord_note in chord:
                interval = Notes.Note.get_interval(beat_note.__class__, chord_note)
                result += self.rewards[interval]

        return result
