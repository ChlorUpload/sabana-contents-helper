from typing import List
from fastapi import FastAPI, Response
from converter import clear_convert_results
from main import convert
from process_option_model import ProcessOptionModel

app = FastAPI()


@app.post("/convert")
def convert_musicxml(title: str,
                     musicxml: str,
                     options: List[ProcessOptionModel]):
    zip_stream = convert(title, musicxml, options)
    zip_filename = f"{title}.zip"
    resp = Response(zip_stream.getvalue(),
                    mimetype="application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    clear_convert_results()
    return resp