from .base import Vocabulary, WordFilter
from .compose_filter import ComposeFilter
from .length_range_filter import LengthRangeFilter
from .spacy_vocab import SpacyVocab
from .selection_filter import SelectionFilter


def unscramble(chars: str) -> set[str]:
    word_filter: WordFilter = ComposeFilter([
        LengthRangeFilter(minimum=3, maximum=len(chars)),
        SelectionFilter(chars),
    ])

    vocab: Vocabulary = SpacyVocab()

    return set(filter(word_filter.test, vocab))
