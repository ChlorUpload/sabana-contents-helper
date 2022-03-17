from ast import Str
from typing import Optional
import music21
import uuid
import os

from stream import musicxml_to_stream

convert_result_path = "./convert_results"


def convert_to_midi(stream: music21.stream.Stream, name: Optional[Str] = None):
    if not os.path.exists(convert_result_path):
        os.mkdir(convert_result_path)
    filename = f"{convert_result_path}/{uuid.uuid4()}_midi_{name}.midi"
    midi_path = stream.write('midi', fp=filename)
    return midi_path


def convert_to_image(stream: music21.stream.Stream, name: Optional[Str] = None):
    if not os.path.exists(convert_result_path):
        os.mkdir(convert_result_path)
    filename = f"{convert_result_path}/{uuid.uuid4()}_image_{name}.png"
    image_path = stream.write('musicxml.png', fp=filename)
    return image_path


def convert_to_musicxml(stream: music21.stream.Stream, name: Optional[Str] = None):
    if not os.path.exists(convert_result_path):
        os.mkdir(convert_result_path)
    filename = f"{convert_result_path}/{uuid.uuid4()}_musicxml_{name}.musicxml"
    musicxml_path = stream.write('musicxml', fp=filename)
    return musicxml_path


def clear_convert_results():
    if os.path.exists(convert_result_path):
        for file in os.scandir(convert_result_path):
            os.remove(file.path)


if __name__ == '__main__':
    stream = musicxml_to_stream('./test-data/part0.musicxml')
    convert_to_midi(stream, 'part0')
