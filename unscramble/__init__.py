import os
from collections import Counter
from typing import Iterable

import nltk  # type: ignore
from nltk.downloader import download  # type: ignore

NLTK_DATA = os.getenv('NLTK_DATA')

download('words', download_dir=NLTK_DATA)
nltk.data.path.append(NLTK_DATA)

wordlist: Iterable[str] = nltk.corpus.words.words()


def unscramble(chars: str) -> set[str]:
    chars = chars.replace(' ', '').lower()

    puzzle_letters = Counter(chars)
    required_letters = list(chars)

    results = set()
    for word in wordlist:
        if 2 < len(word) <= len(chars) and Counter(word) <= puzzle_letters:
            for letter in required_letters:
                if letter in word:
                    results.add(word)

    return results
