# Unit 600.1 - Video: Strings

Any sequence of *characters*. A *string* of characters

Including:
- letters
- numbers
- specials characters
- punctuation
- spaces
- etc

**Declaring Strings in Python**

Strings are declared between quotation marks "hello world" or single quotation marls 'hello world'
Strings can be *concatenated* together in *expressions*:

**String Concatenation**

```python
name = 'foo'
surname = 'bar'
full_name = name + surname
print(full_name)
# foobar
```

\*an operator, such as the `+` operator, is said to be *overloaded* when it behaves differently in different contexts [^1]
i.e: given different set of types, the procedure which the operator performs is dependent on the given types

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

### Unit 600.1 - Video: Input/Output

**Displaying Text on Screen**

The `print` function allows you to display values to the screen

```print
x = 'foobar'
print(x)
# foobar
```

The `print` function can an arbitrary amount of arguments and will concatenate a space to each individual argument before displaying it onscreen
It also converts each individual parameter into a string

```python
a = 'foo'
b = 'bar'
c = 'baz'
print(a, b ,c)
# foo bar baz

d = 1
e = 2
print(a, b, c, d, e)
# foo bar baz 1 2
```

**Reading Input from User**

The `input` function will allow the user of the python script to input text, and will then store the input into a variable
The stored input will be of type `str`:

```python
a = input('Input some text: ')
# Input some text: 
# foo

print(a) # foo
print(type(a)) # str

b = input('Input a number: ')
# Input a number:
# 42069

print(b) #42069
print(type(b)) # str
```

The type of `input` will always be stored as a `str`
If the user input needs to be interpreted as another type, the explicit casts need to be performed

___

### Unit 600.1 - Video: IDEs

**IDE - Integrated Development Environment**

A consolidated set of tools to assist with the development process
Consists primarily of:
 - A text editor
 - A shell
 - Tools for debugging and proofing your code
 - Convenient tools for managing, editing, and executing your code

___

### Unit 600.1 - Video: Control Flow

**Program Control Flow**

`if`, `elif`, and `else` are example of Python branching syntax.
Used for testing user-defined predicates to control flow of program

**Control Flow using loops**

The `while` keyword is used to perform a block of code *while* a certain predicate is true:

Syntax:
```python
while <condition>:
	<expression>
	...
```

Eg: Print a number while it is less than 5:

```python
n = 0
while n < 5:
	n += 1
```

The `for` keyword is syntactic sugar for a `while` loop that tests a predicate and increments/modifies the control variable for the loop's condition

Eg:
```python
# This has the same behaviour:
n = 0
while n < 0:
	n += 1
	
# as:
for n in range(5):
	# n's value is handled by the range function
```

The `range()` function is a generator function that returns a set of values in a list
Accepts up to three arguments:
- range(start, end, step)

The `in` keyword accesses values in a list in the context of a loop

The `break` keyword can be used inside of a loop-block to escape the loop:
```python
for n in range(100):
	if n == 25:
		break
	print(n)
```

**Conceptual Uses for `while` and `for` loops**

The `for` loop is primarily used when the amount of iterations can be determined before the loop is invoked
- Control variables are initialized at the `for` loop declaration
- Control variables are automatically modified at the end of each iteration of the loop-block

The `while` loop is used to loop when the amount of iterations cannot is not known ahead of entering the loop-block
- Control variables must be initialized prior to entering the loop-block
- Control variables must be modified inside of the loop-block

___

### Unit 600.1 - Video: Iteration

Branching structures operate in *constant time* because it only executes once
Iteration allows us to use the same block of code multiple times, therefore, it operates in time that is proportional to the amount of iterations

___

### Unit 600.1 - Video: Guess and Check

**Classes of Algorithms**

*guess-and-check* method:
- Guess or *generate* some variable to *test* against for certain criteria
- Keep iterating and generating new guesses until the *test* passes
- This process is a part of a class of algorithms called *exhaustive enumeration* [^2]

Eg: Cube root using a *guess-and-check* approach
```python
cube = 27
for guess in range(abs(cube + 1)):
	if guess ** 3 >= abs(cube):
		break
		
	if guess ** 3 != abs(cube):
		print(cube, 'is not a perfect cube')
		
	else:
		if cube < 0:
			guess = -guess
			
		print('Cube root of', cube, 'is', guess)
```

___
[^1]: [Operator overloading - Wikipedia](https://en.wikipedia.org/wiki/Operator_overloading)
[^2]: [Brute-force search - Wikipedia](https://en.wikipedia.org/wiki/Brute-force_search)
