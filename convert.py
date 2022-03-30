from io import BytesIO
from typing import List
from converter import clear_convert_results, convert_to_image, convert_to_midi, convert_to_musicxml
from process_option_model import ProcessOptionModel
from stream import apply_option, musicxml_to_stream
from zipfiles import zipfiles
import sys
from pathlib import Path
import json


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

            image_path = convert_to_image(applied_stream)
            image_file = {
                "name": f"{name}_{hand}.png",
                "path": image_path
            }
            files.append(image_file)

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
        # ProcessOptionModel(name="fronter",
        #                    start_measure=0,
        #                    end_measure=4),
        # ProcessOptionModel(name="back",
        #                    start_measure=4,
        #                    end_measure=None),
        ProcessOptionModel(name="whole",
                           start_measure=None,
                           end_measure=None),
    ]

    if len(sys.argv) == 3:
        argv1 = sys.argv[1]
        argv2 = sys.argv[2]
        if Path(argv1).suffix == ".musicxml":
            musicxml = argv1
            info = argv2
        else:
            musicxml = argv2
            info = argv1

        title = Path(musicxml).stem

        with open(info, "rt", encoding="utf8") as f:
            info = json.load(f)
            options = []
            part = 0
            for range in info:
                part += 1
                start = range["start"]
                end = range["end"] + 1
                options.append(ProcessOptionModel(
                    name=f"part{part}", start_measure=start, end_measure=end))

    byte_stream = convert(title, musicxml, options)

    with open("./result.zip", "wb") as f:
        f.write(byte_stream.getvalue())
