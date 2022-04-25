from typing import Iterator

import nltk  # type: ignore
from nltk.downloader import download  # type: ignore

from .base import Vocabulary


class NLTKVocabulary(Vocabulary):
    def __init__(self, path: str | None = None, *, downloaded: bool = False) -> None:
        self.path = path
        self.words: list[str] = []
        self._downloaded = downloaded

    def _is_loaded(self) -> bool:
        return self._downloaded

    def _load(self) -> None:
        download('words',
                 download_dir=self.path,
                 prefix=f'[{self.__class__.__qualname__}] ')

        if self.path is not None and self.path not in nltk.data.path:
            nltk.data.path.append(self.path)

        self.words = nltk.corpus.words.words()
        self._downloaded = True

    def __iter__(self) -> Iterator[str]:
        if not self._is_loaded():
            self._load()
        yield from self.words
