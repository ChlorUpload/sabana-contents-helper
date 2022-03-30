import os
import sys


def inline_xml(path: str):
    result = ""
    with open(path, "rt", encoding="utf8") as f:
        strs = f.readlines()
        for str in strs:
            str = str.strip(' ')
            str = str.replace('\n', '')
            str = str.replace('"', '\\"')
            result += str
    return result


if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        with open("./result.txt", "wt") as f:
            f.write(inline_xml(path))
