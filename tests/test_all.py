"""Test module."""
import pytest

from libfuncpy import give, make_iterable


def test_give():
    """Test give closure."""
    one = give(1)
    assert 1 == one()


@pytest.mark.parametrize(
    'value,expected',
    [
        (1, [1]),
        ]
    )
def test_make_iterable_non_iterables(value, expected):
    """Test make iterable."""
    assert make_iterable(value) == expected


@pytest.mark.parametrize(
    'value',
    [
        'asd',
        [1, 2],
        (i for i in range(10)),
        [],
        ]
    )
def test_make_iterable_pass(value):
    """Test make iterable."""
    assert make_iterable(value) is value
