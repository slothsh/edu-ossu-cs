# Unit 600.1 - Video: Bindings

There are certain words that cannot be as used as variables.
They're called 'keywords'. They have special meaning in the language

Eg:
- `float`
- `str`
- `int`
- `if`
- `elif`
- `else`
- etc...

You can't swap variables in python like you'd expect in mathematics:

```python
x = 1
y = 2
y = x
x = y
```

Both x and y will be equals to 1, in the above case.
Python will always obey the sequence of operations. i.e any new value bindings to a name will follow through the sequence

You could swap the variables the following way:

```python
x = 1
y = 2
temp = y
y = x
x = temp
```

___
