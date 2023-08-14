# MIT 600.1 - Lecture 2

Instructor: Dr. Ana Bell

Video: Branching and Iteration

Link: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-2-branching-and-iteration/

**Program Control Flow**

`if`, `elif`, and `else` are example of Python branching syntax.

Used for testing user-defined predicates to control flow of program.

**Control Flow using loops**

The `while` keyword is used to perform a block of code *while* a certain predicate is true.

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

The `for` keyword is syntactic sugar for a `while` loop that tests a predicate
and increments/modifies the control variable for the loop's condition.

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

The `range()` function is a generator function that returns a set of values in
a list Accepts up to three arguments:

- range(start, end, step)

The `in` keyword accesses values in a list in the context of a loop.

The `break` keyword can be used inside of a loop-block to escape the loop:

```python
for n in range(100):
	if n == 25:
		break
	print(n)
```

**Conceptual Uses for `while` and `for` loops**

The `for` loop is primarily used when the amount of iterations can be
determined before the loop is invoked:

- Control variables are initialized at the `for` loop declaration
- Control variables are automatically modified at the end of each iteration of the loop-block

The `while` loop is used to loop when the amount of iterations cannot is not
known ahead of entering the loop-block:

- Control variables must be initialized prior to entering the loop-block
- Control variables must be modified inside of the loop-block

___
