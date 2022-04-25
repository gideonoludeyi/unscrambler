from abc import ABC, abstractmethod
from collections.abc import Container, Iterable


class Vocabulary(Container[str], Iterable[str]):
    def __contains__(self, word: object) -> bool:
        return isinstance(word, str) and any(word == w for w in self)


class WordFilter(ABC):
    @abstractmethod
    def test(self, word: str) -> bool:
        raise NotImplementedError
