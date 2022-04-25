import os

from .base import Vocabulary, WordFilter
from .length_range_filter import LengthRangeFilter
from .nltk_vocab import NLTKVocabulary
from .selection_filter import SelectionFilter
from .compose_filter import ComposeFilter

NLTK_DATA = os.getenv('NLTK_DATA')


def unscramble(chars: str) -> set[str]:
    word_filter: WordFilter = ComposeFilter([
        LengthRangeFilter(minimum=3, maximum=len(chars)),
        SelectionFilter(chars),
    ])

    vocab: Vocabulary = NLTKVocabulary(path=NLTK_DATA)

    return {word for word in vocab if word_filter.test(word)}
