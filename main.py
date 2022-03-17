from typing import List
from fastapi import FastAPI, Response
from converter import convert_to_midi
from process_option_model import ProcessOptionModel
from stream import apply_option, musicxml_to_stream
from zipfiles import zipfiles


app = FastAPI()


@app.post("/convert")
def convert_musicxml(title: str,
                     musicxml: str,
                     options: List[ProcessOptionModel]):

    stream = musicxml_to_stream(musicxml)

    files = []
    for option in options:
        name = option.name
        applied_stream = apply_option(stream, option)
        midi_path = convert_to_midi(applied_stream)
        midi_file = {
            "name": f"{name}_midi",
            "path": midi_path
        }

        files.append(midi_file)

    zip_filename = "%s.zip" % title
    s = zipfiles(files, title)
    resp = Response(s.getvalue(), mimetype="application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp


if __name__ == "__main__":
    stream = musicxml_to_stream("./test-data/part0.musicxml")
    options = [
    
    ]

    files = []
    for option in options:
        name = option.name
        applied_stream = apply_option(stream, option)
        midi_path = convert_to_midi(applied_stream)
        midi_file = {
            "name": f"{name}_midi",
            "path": midi_path
        }

        files.append(midi_file)

    zip_filename = "%s.zip" % title
    s = zipfiles(files, title)
    resp = Response(s.getvalue(), mimetype="application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp

