* It may seem convenient to return `None` from your functions when the input values result in a strange result, e.g. division by zero.
* Knowing that this function returns `None`, callers of the function may include code to handle this case like so: `if not result:`. In this case, though, our function may return a valid value of 0, which also evaluates to `None`. 
* There are a few ways to handle this case, but one of the most clear is raising an exception (see the `divide` function in this directory).
* The `raise Exception from e` syntax can be helpful for identifying the root cause of the exception in a traceback. [See this reference](https://stackoverflow.com/questions/24752395/python-raise-from-usage).
