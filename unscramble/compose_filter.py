from typing import Iterable
from .base import WordFilter


class ComposeFilter(WordFilter):
    def __init__(self, filters: Iterable[WordFilter], /) -> None:
        self.filters = filters

    def test(self, word: str) -> bool:
        return all(f.test(word) for f in self.filters)
