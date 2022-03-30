from typing import List
from fastapi import FastAPI, Response
from pydantic import BaseModel
from converter import clear_convert_results
from convert import convert
from process_option_model import ProcessOptionModel

app = FastAPI()


class ConvertInfoModel(BaseModel):
    title: str
    musicxml: str
    options: List[ProcessOptionModel]


@app.post("/convert")
def convert_musicxml(convertInfo: ConvertInfoModel):
    title = convertInfo.title
    musicxml = convertInfo.musicxml
    options = convertInfo.options
    zip_stream = convert(title, musicxml, options)
    zip_filename = f"{title}.zip"
    resp = Response(zip_stream.getvalue(), media_type="application/x-zip-compressed", headers={
        'Content-Disposition': f'attachment;filename={zip_filename}'
    })

    clear_convert_results()
    return resp
