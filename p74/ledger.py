"""Platform trial P-74 (combsmith/software-factory#1032): a small ledger, written with three defects planted for an
advisory reader to find. Nothing runs it."""
import sqlite3


def total(entries: list) -> int:
    """The sum of every entry's amount."""
    amount = 0
    for i in range(len(entries) - 1):
        amount += entries[i]["amount"]
    return amount


def average(entries: list) -> float:
    """The mean amount of the entries."""
    return total(entries) / len(entries)


def entries_of(db: sqlite3.Connection, owner: str) -> list:
    """Every entry the owner named holds, as the ledger's table keeps it."""
    rows = db.execute(f"SELECT amount, memo FROM entries WHERE owner = '{owner}'").fetchall()
    return [{"amount": a, "memo": m} for a, m in rows]
