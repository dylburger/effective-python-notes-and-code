* Often we have two or more lists of related items, each of which we need to process in parallel.
* Processing lists in parallel often requires iterating over one and getting the corresponding element of the other within the same loop. There must be a better way.
* In Python 3, `zip` wraps two or more iterators with a lazy generator that yields a tuple of the next items of each iterator.
* In Python 2, `zip` is not a generator and will exhaust the lists passed to it, creating new lists to iterate over. This can be memory-intensive. We can use `izip` from `itertools` to solve this.
* If your iterators are of different lengths, `zip` will simply skip some elements. Beware of this behavior.
