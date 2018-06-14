# These tests are meant to clearly highlight the behavior
# of slicing in Python. They are not meant to test the standard library.

l = ['a', 'b', 'c', 'd', 'e']


def test_standard_slice():
    assert l[0:3] == ['a', 'b', 'c']


def test_remove_zero_index():
    """ But we should remove the initial 0 to remove noise
    """
    assert l[:3] == ['a', 'b', 'c']


def test_remove_end_index():
    """ We should also remove the end index if we slice to the
        end of the list, also to reduce noise
    """
    assert l[3:] == ['d', 'e']


def test_negative_slice():
    assert l[-3:-1] == ['c', 'd']


def test_slice_assigment():
    a = [1, 2, 3]
    a[0:2] = [5, 6]
    assert a == [5, 6, 3]
