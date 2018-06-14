import stride_funcs


def test_reverse_list():
    assert stride_funcs.reverse_list([1, 2, 3]) == [3, 2, 1]
