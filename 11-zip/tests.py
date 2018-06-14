names = ['Dylan', 'Danny', 'Chris']
birthdays = ['Jan 1', 'Jan 2', 'Jan 3']
ages = [31, 32, 33]


def test_zipping_two_lists():
    assert next(zip(names, birthdays)) == ('Dylan', 'Jan 1')


def test_zipping_three_lists():
    assert next(zip(names, birthdays, ages)) == ('Dylan', 'Jan 1', 31)
