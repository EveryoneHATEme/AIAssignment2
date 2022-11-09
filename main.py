import mido
from pprint import pprint
from operator import attrgetter

from Track import Track
from TimeSignature import TimeSignature
from GeneticAlgorithm import GeneticAlgorithm


def main():
    file = mido.MidiFile('midi/input1.mid')

    time_signature_message = list(filter(lambda x: x.type == 'time_signature', file.tracks[0]))
    if not time_signature_message:
        return

    time_signature = TimeSignature(time_signature_message[0].numerator, time_signature_message[0].denominator)

    track = Track(file.tracks[1], time_signature, file.ticks_per_beat)

    obtained = GeneticAlgorithm(track).evolution()

    new_track = file.add_track(file.tracks[1].name)
    new_track.append(mido.Message('program_change', channel=0, program=0, time=0))

    mean_octave = sum(map(attrgetter('octave'), track.notes)) // len(track.notes)

    for chord in obtained:
        for note in chord.notes:
            new_track.append(mido.Message('note_on',
                                          channel=0,
                                          note=note.get_note_key(mean_octave - 1),
                                          velocity=50,
                                          time=0))
        for i, note, in enumerate(chord.notes):
            new_track.append(mido.Message('note_off',
                                          channel=0,
                                          note=note.get_note_key(mean_octave - 1),
                                          velocity=0,
                                          time=track.ticks_per_beat if i == 0 else 0))

    new_track.append(mido.MetaMessage('end_of_track', time=0))
    file.save('midi/output.mid')


if __name__ == '__main__':
    main()
