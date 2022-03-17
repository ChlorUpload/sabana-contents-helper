import os
from typing import Dict
import zipfile
from io import BytesIO


def zipfiles(files: Dict, zip_subdir) -> BytesIO:
    bytesIO = BytesIO()
    zf = zipfile.ZipFile(bytesIO, "w")

    for file in files:
        name = file["name"]
        path = file["path"]
        zip_path = os.path.join(zip_subdir, name)
        zf.write(path, zip_path)

    zf.close()
    return bytesIO
