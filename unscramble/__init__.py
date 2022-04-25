from .base import Vocabulary, WordFilter
from .compose_filter import ComposeFilter
from .length_range_filter import LengthRangeFilter
from .selection_filter import SelectionFilter
from .spacy_vocab import SpacyVocab


def unscramble(chars: str) -> set[str]:
    word_filter: WordFilter = ComposeFilter([
        LengthRangeFilter(minimum=3, maximum=len(chars)),
        SelectionFilter(chars),
    ])

    vocab: Vocabulary = SpacyVocab()

    return set(filter(word_filter.test, vocab))
