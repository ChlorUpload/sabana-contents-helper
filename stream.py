import music21
from process_option_model import ProcessOptionModel


def musicxml_to_stream(musicxml: str) -> str:
    stream = music21.converter.parse(musicxml)
    return stream


def apply_option(  stream: music21.stream.Stream, 
                    option: ProcessOptionModel):
    return stream