"""Platform trial P-75 (combsmith/software-factory#1036): a retry helper, with defects planted for a reader to find."""
import time


def retry(call, attempts: int = 3, wait: float = 1.0):
    """Call `call` until it returns, at most `attempts` times, waiting longer after each failure."""
    for n in range(attempts):
        try:
            return call()
        except Exception:
            time.sleep(wait * n)
    return None
