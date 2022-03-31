from io import BytesIO
from typing import List
from converter import clear_convert_results, convert_to_image, convert_to_midi, convert_to_musicxml
from process_option_model import ProcessOptionModel
from stream import apply_option, musicxml_to_stream
from zipfiles import zipfiles
from pathlib import Path

from music21 import *
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/usr/bin/mscore'
us['directoryScratch'] = '/tmp'


def convert(title: str, musicxml: str, options: List[ProcessOptionModel]) -> BytesIO:
    stream = musicxml_to_stream(musicxml)
    files = []

    for hand in ["left", "right", "both"]:
        for option in options:
            name = option.name
            applied_stream = apply_option(stream, option, hand)

            midi_path = convert_to_midi(applied_stream)
            midi_file = {
                "name": f"{name}_{hand}.midi",
                "path": midi_path
            }
            files.append(midi_file)

            try:
                image_path = convert_to_image(applied_stream)
                image_file = {
                    "name": f"{name}_{hand}.png",
                    "path": image_path
                }
                files.append(image_file)
            except:
                pass

            musicxml_path = convert_to_musicxml(applied_stream)
            musicxml_file = {
                "name": f"{name}_{hand}.musicxml",
                "path": musicxml_path
            }
            files.append(musicxml_file)

    return zipfiles(files, title)


if __name__ == "__main__":
    clear_convert_results()

    title = "demo"
    musicxml = f"./test-data/{title}.musicxml"
    options = [
        ProcessOptionModel(name="whole",
                           start_measure=1,
                           end_measure=4),
    ]

    byte_stream = convert(title, musicxml, options)

    print("done!")

    with open("./result.zip", "wb") as f:
        f.write(byte_stream.getvalue())
