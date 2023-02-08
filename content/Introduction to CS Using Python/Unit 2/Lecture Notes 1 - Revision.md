# MIT 600.2 - Video: Revision

**Strings**

A sequence of case-sensitive characters
Strings can be compared: `==`, `>`, `<`
A string's length can be retrieved with the `len()` function
String's can be indexed using the `[]` operator
String's can also be sliced with the `[::]` operator, as well
Strings are immutable - they cannot be mutated with a different value after they've been declared.
Strings are *iterable* - which means they have first-class support in for-loops:

```python
s = 'foo'
for c in s:
	print(c)
	
# f
# o
# o

```

You can use a string as the input argument of the `in` keyword, directly. The return value of the `in` keyword will return each individual character in the string in loop-block.

___
