* We can slice any class that implements a `__getitem__` and `__setitem__` method.
* Slices return a new list. Modifying this new slice will not affect the original list, since it's a copy.
* When using slices in assignment, it will affect the original list (see `tests.py`).
