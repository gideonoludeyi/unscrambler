from typing import Iterable, Iterator

import en_core_web_sm  # type: ignore

from .base import Vocabulary


class SpacyVocab(Vocabulary):
    def __init__(self) -> None:
        self.words: Iterable[str] = []
        self._loaded = False

    def _is_loaded(self) -> bool:
        return self._loaded

    def _load(self) -> None:
        nlp = en_core_web_sm.load()
        self.words = nlp.vocab.strings
        self._loaded = True

    def __iter__(self) -> Iterator[str]:
        if not self._is_loaded():
            self._load()
        yield from self.words
