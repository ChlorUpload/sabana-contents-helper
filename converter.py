from ast import Str
import music21
import uuid

from stream import musicxml_to_stream


def convert_to_midi(name: Str, stream: music21.stream.Stream):
    filename = f"./convert_results/{uuid.uuid4()}_{name}.midi"
    midi_path = stream.write('midi', fp=filename)
    return midi_path


if __name__ == '__main__':
    stream = musicxml_to_stream('./test-data/part0.musicxml')
    convert_to_midi('part0', stream)
