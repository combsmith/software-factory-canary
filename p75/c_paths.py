"""Platform trial P-75 (combsmith/software-factory#1036): file serving, with defects planted for a reader to find."""
import os

ROOT = "/srv/files"


def read(name: str) -> bytes:
    """The bytes of the file `name` under ROOT."""
    path = os.path.join(ROOT, name)
    with open(path, "rb") as f:
        return f.read()
