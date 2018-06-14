import stride_funcs


def test_reverse_list():
    assert stride_funcs.reverse_list([1, 2, 3]) == [3, 2, 1]


def test_odd_elements():
    assert stride_funcs.get_elements_at_odd_indices([1, 2, 3]) == [1, 3]


def test_even_elements():
    assert stride_funcs.get_elements_at_even_indices([1, 2, 3]) == [2]
