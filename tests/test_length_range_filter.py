import pytest  # type: ignore
from unscramble.length_range_filter import LengthRangeFilter


@pytest.fixture
def words():
    return ['apple', 'orange', 'banana', 'cherry', 'watermelon',
            'lime', 'lemon', 'avocado', 'cucumber', 'date']


def test_should_be_true_for_only_the_words_whose_length_are_between_minimum_and_maximum_inclusive(words: list[str]) -> None:
    word_filter = LengthRangeFilter(minimum=5, maximum=8)
    result = {word for word in words if word_filter.test(word)}
    expected = {'apple', 'orange', 'banana',
                'cherry', 'lemon', 'avocado', 'cucumber'}
    assert result == expected


def test_should_be_true_for_only_the_words_whose_length_are_the_specified_minimum_or_above(words: list[str]) -> None:
    word_filter = LengthRangeFilter(minimum=6)
    result = {word for word in words if word_filter.test(word)}
    expected = {'orange', 'banana', 'cherry',
                'watermelon', 'avocado', 'cucumber'}
    assert result == expected


def test_should_be_true_for_only_the_words_whose_length_are_between_0_and_the_maximum_inclusive(words: list[str]) -> None:
    word_filter = LengthRangeFilter(maximum=8)
    result = {word for word in words if word_filter.test(word)}
    expected = {'apple', 'orange', 'banana', 'cherry',
                'lime', 'lemon', 'avocado', 'cucumber', 'date'}
    assert result == expected


def test_should_be_false_for_all_the_words_when_the_minimum_is_greater_than_the_maximum(words: list[str]) -> None:
    word_filter = LengthRangeFilter(minimum=4, maximum=2)
    result = {word for word in words if word_filter.test(word)}
    expected: set[str] = set()
    assert result == expected


def test_should_be_false_for_all_the_words_when_the_maximum_is_non_positive(words: list[str]) -> None:
    word_filter = LengthRangeFilter(minimum=-4, maximum=-1)
    result = {word for word in words if word_filter.test(word)}
    expected: set[str] = set()
    assert result == expected
