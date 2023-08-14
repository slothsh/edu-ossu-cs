# MIT 600.1 - Lecture 2

Instructor: Dr. Ana Bell

Video: Branching and Iteration

Link: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-2-branching-and-iteration/

Any sequence of *characters*. A *string* of characters

Including:
- letters
- numbers
- specials characters
- punctuation
- spaces
- etc

**Declaring Strings in Python**

Strings are declared between quotation marks "hello world" or single quotation
marls 'hello world'

Strings can be *concatenated* together in *expressions*:

**String Concatenation**

```python
name = 'foo'
surname = 'bar'
full_name = name + surname
print(full_name)
# foobar
```

An operator, such as the `+` operator, is said to be *overloaded* when it
behaves differently in different contexts [^1] i.e: given different set of
types, the procedure which the operator performs is dependent on the given
types

**String Successive Concatenation**

Strings can be duplicated using the string *overloaded* \* * operator:

```python
name = 'foo'
namedup = 5 * name
print(namedup)
# foofoofoofoofoo
```

**Length of a String**

The `len()` function returns a count of characters in a string:

```python
name = 'foo'
namelen = len(name)
print(namelen)
# 3
```

**Indexing into a String**

Indexing is *zero-based*
i.e: indexing strings, and all other indexed data types, starting from zero.

```python
name = 'foo'
char1 = name[0]
char2 = name[1]
char3 = name[2]
print(char1, char2, char3)
# f o o
```

Strings can also be indexed in reverse using negative numbers as input to the `[]` operator

```python
name ='foo'
c1 = name[-1] # o
c2 = name[-2] # o
c3 = name[-3] # f
```

**Ranged Indexing into String**

Ranges, or sub-strings, some string A can be accessed using the range-index syntax of Python:
This operation is also called *slicing*

```python
name = 'foo'
sstr1 = name[0:] # foo
sstr2 = name[1:] # oo
sstr3 = name[-3:] # foo
sstr4 = name[:] # foo
```

All of the above are copies of the original data inside of the 'name' binding.

Slicing accesses the contents of a string with a semi-closed interval: \[i:j\)
Which is to say that the value of the starting index is included in the slice, while the end index is non-inclusive:

```python
s = 'foobar'
sfoo = s[0:3] # foo
sfo = a[0:2] # fo
```

The slicing operator, \[\], has a third argument which can be used to specify the step size of the slice:

```python
s = 'foobarbazbar'
sstr1 = s[::2] # foabza
sstr = s[::3] # fbbb
```

The `in` and `not in` operators are used to test for collection membership in python data types such as *lists*, *tuples* and *dictionaries*
The operators return a Bool if the element *e* exists in any collection *C*:

```python
C = [0, 1, 2, 3, 4]
e = 3
exists = e in C # True
e = 12
exists = e in C # False
e = 42
exits = e not in C # True
```

___

[^1]: [Operator overloading - Wikipedia](https://en.wikipedia.org/wiki/Operator_overloading)

