import mido
from pprint import pprint

from Track import Track
from TimeSignature import TimeSignature


def main():
    file = mido.MidiFile('midi/barbiegirl_mono.mid')

    time_signature_message = list(filter(lambda x: x.type == 'time_signature', file.tracks[0]))
    if not time_signature_message:
        return

    time_signature = TimeSignature(time_signature_message[0].numerator, time_signature_message[0].denominator)

    track = Track(file.tracks[1], time_signature, file.ticks_per_beat)

    pprint(track.get_beats())


if __name__ == '__main__':
    main()
