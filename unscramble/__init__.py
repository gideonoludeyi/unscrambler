import os

from .base import Vocabulary, WordFilter
from .length_range_filter import LengthRangeFilter
from .nltk_vocab import NLTKVocabulary
from .selection_filter import SelectionFilter

NLTK_DATA = os.getenv('NLTK_DATA')


def unscramble(chars: str) -> set[str]:
    length_filter: WordFilter = LengthRangeFilter(
        minimum=3, maximum=len(chars))
    character_bound_filter: WordFilter = SelectionFilter(chars)

    vocab: Vocabulary = NLTKVocabulary(path=NLTK_DATA)

    return {word for word in vocab if length_filter.test(word) and character_bound_filter.test(word)}
