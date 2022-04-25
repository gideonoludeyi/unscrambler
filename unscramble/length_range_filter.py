from .base import WordFilter


class LengthRangeFilter(WordFilter):
    def __init__(self, *, minimum: int = 0, maximum: int = 100_000) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def test(self, word: str) -> bool:
        return self.minimum <= len(word) <= self.maximum
