* One problem with list comprehensions: they create a whole new list. For large lists, this could be problematic.
* Generator expressions combine the logic of list comprehensions and generators, creating an iterator that yields only one item at a time.
* We can import Python types (e.g. for use in `isinstance`). Here we can use the `GeneratorType` to confirm that the generator expression results in a generator.
* Generators are great tools for iterating over large streams of input.
* **One caveat**: generators are stateful, so you can only iterate over them once.
