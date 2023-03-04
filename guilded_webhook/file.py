import mimetypes
import os

from .exceptions import UnknownMimeType

from typing import Union, Any
import io

class File: # roughly based on discord.py's discord.File
    def __init__(self, fp: Union[str, bytes, os.PathLike, io.BufferedIOBase], filename: str=None) -> None:
        if isinstance(fp, io.IOBase):
            if not (fp.seekable() and fp.readable()):
                raise ValueError(f'File buffer {fp!r} must be seekable and readable')
            self.fp: io.BufferedIOBase = fp
        else:
            self.fp = open(fp, 'rb')
        
        if filename is None:
            if isinstance(fp, str):
                _, filename = os.path.split(fp)
            else:
                filename = getattr(fp, 'name', 'untitled')
        
        self.filename = filename

        mt = mimetypes.guess_type(self.filename)
        if mt:
            self.content_type = mt[0]
        else:
            raise UnknownMimeType(f"Failed to determine mimetype of {self.filename}")

    def read(self):
        return self.fp.read()

    def __repr__(self) -> str:
        return self.filename