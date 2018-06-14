import pytest
from divide import divide


def test_divide_normal_args():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
