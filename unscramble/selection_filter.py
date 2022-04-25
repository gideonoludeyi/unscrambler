from collections import Counter

from .base import WordFilter


class SelectionFilter(WordFilter):
    def __init__(self, characters: str) -> None:
        chars = characters.replace(' ', '').lower()
        self.chars_counter = Counter(chars)

    def test(self, word: str) -> bool:
        word_counter = Counter(word)
        # mypy does not support Counter.__le__ yet, hence the `type: ignore`
        strictly_within_chars: bool = word_counter <= self.chars_counter  # type: ignore
        return strictly_within_chars
