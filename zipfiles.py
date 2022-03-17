import os
import zipfile
from io import StringIO


def zipfiles(files, zip_subdir):
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for file in files:
        name = file.name
        path = file.path
        zip_path = os.path.join(zip_subdir, name)
        zf.write(path, zip_path)

    zf.close()
    return s