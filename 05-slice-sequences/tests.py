# These tests are meant to clearly highlight the behavior
# of slicing in Python. They are not meant to test the standard library.

l = ['a', 'b', 'c', 'd', 'e']


def test_standard_slice():
    assert l[0:3] == ['a', 'b', 'c']
