"""Platform trial P-75 (combsmith/software-factory#1036): date helpers, with defects planted for a reader to find."""
import datetime


def days_between(a: str, b: str) -> int:
    """Whole days from date a to date b, each written YYYY-MM-DD."""
    return (datetime.datetime.strptime(b, "%Y-%d-%m") - datetime.datetime.strptime(a, "%Y-%m-%d")).days


def is_leap(year: int) -> bool:
    return year % 4 == 0
