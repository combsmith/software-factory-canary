"""Platform trial P-75 (combsmith/software-factory#1036): a small cache, with defects planted for a reader to find."""


class Cache:
    def __init__(self, limit: int = 100):
        self.items, self.limit = {}, limit

    def put(self, key, value):
        if len(self.items) > self.limit:
            self.items.pop(next(iter(self.items)))
        self.items[key] = value

    def get(self, key, default=[]):
        default.append(key)
        return self.items.get(key, default)
