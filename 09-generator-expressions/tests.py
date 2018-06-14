from types import *


def test_generator_expression():
    it = (len(line) for line in open('file.txt'))
    assert isinstance(it, GeneratorType)


def test_next_method():
    it = (len(line) for line in open('file.txt'))
    assert next(it) == 15
