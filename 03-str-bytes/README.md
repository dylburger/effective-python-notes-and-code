UTF-8 allows us to represent Unicode characters as binary data (in 8-bit values).

Use the `encode()` method to convert Unicode to the associated binary data.

Use the `decode()` method to convert bytes to Unicode strings.

Recommendation: use Unicode string types within our program, assuming nothing about the character encoding. Encode and decode at the furthest boundaries of our program.

Always output UTF-8 as our text encoding.

`bytes` and `str` values are never equivalent in Python 3 (even in the case of an empty string), so we must handle types carefully when passing values around.

When we write data to files in Python 3, the default value of the encoding argument is `utf-8` for the `open` function. This means that `f.write()` expects data of type `str`. If we try to pass binary data (`bytes`), it will fail. This will fix this:

    with open(file, 'wb') as f:
        f.write(my_bytes)
