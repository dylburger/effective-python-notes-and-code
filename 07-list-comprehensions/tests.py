def test_basic_list_comprehension():
    li = [1, 2, 3]
    assert [el * 2 for el in li] == [2, 4, 6]


def test_enumerate_list_comprehension():
    li = [1, 2, 3, 4, 5]
    assert [el for i, el in enumerate(li) if i > 2] == [4, 5]
