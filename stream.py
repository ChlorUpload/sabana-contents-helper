from typing import Optional
import music21
from process_option_model import ProcessOptionModel


def musicxml_to_stream(musicxml: str) -> str:
    stream = music21.converter.parse(musicxml)
    return stream


def apply_option(stream: music21.stream.Stream,
                 option: ProcessOptionModel,
                 hand: Optional[str] = None):
    if hand == None:
        hand = "both"

    if option.start_measure == None:
        option.start_measure = 0

    if option.start_measure != None or option.end_measure != None:
        stream = stream.measures(option.start_measure, option.end_measure)

    p0 = stream.parts[0]
    p0._setPartName("")
    p1 = stream.parts[1]
    p1._setPartName("")

    newStream = music21.stream.Score()
    if hand == "right" or hand == "both":
        newStream.insert(0, p0)
    if hand == "left" or hand == "both":
        newStream.insert(0, p1)

    return newStream


if __name__ == '__main__':
    stream = musicxml_to_stream('./test-data/180bpm.musicxml')
    option = ProcessOptionModel(
        name="test", hands="both", start_measure=1, end_measure=4)
    stream = apply_option(stream, option)
