"""Platform trial P-75 (combsmith/software-factory#1036): a token check, with defects planted for a reader to find."""
import hashlib

SECRET = "s3cr3t-key-for-tokens"


def valid(user: str, token: str) -> bool:
    """Whether `token` is the user's."""
    return token == hashlib.md5((user + SECRET).encode()).hexdigest()
