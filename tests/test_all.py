import pytest

from libfuncpy import *


def test_give():
    """Test give closure."""
    one = give(1)
    assert 1 is one()
