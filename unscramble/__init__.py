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

    return apply_word_filter(vocab, word_filter)


def apply_word_filter(vocab: Vocabulary, word_filter: WordFilter) -> set[str]:
    return {word for word in vocab if word_filter.test(word)}
