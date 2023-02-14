# Unit 600.1 - Video: Operators and Branching

**Comparison Operators for ints and floats**

Logical operators take a lhs and rhs and compares them. The return type is a bool

\> - greater than -> returns a True if lhs is greater than rhs
\< - less than -> returns True if lhs is less than rhs
\>\= - greater than and equals -> returns True if lhs is greater than and equals to rhs
\<\= less than and equals -> returns True if lhs is less than and equals to rhs
\=\= equals -> returns True if lhs is exactly equals to rhs
\!\= not equals -> returns True if lhs is anythin but exactly equals to rhs

*and* -> logical and; short-circuits logical expression when any expression evaluates to false
*or* -> logical or; short-circuits logical expression when any expression evaluates to true
*not* -> negates bool

**Conditional Branching in a Program**

A branching program consists of:
- a *test*
- a block of code to execute if the test returns true
- a block of code to execute if the test returns false

Python doesn't require a block of code to perform if the test evaluates to false. It will simply continue with the rest of the program

The *if* operator in Python is used to declare a conditional test
The *else* statement, which must succeed an *if-block* is used to declare the false block of code for a false test

```python
if 1 == 1:
	print('1 is equals to 1')
else:
	print('false block')
```

*if-blocks* can be nested

```python
if True:
	if 1 == 1:
		if 2 == 2:
			print('2 equals 2')
	else:
		print('2 is not equals to 2')
else:
	print('unreachable false block')	
```

*elif* operator, which must succeed an *if-block*, is used to have a follow up test if the preceding *if-block*'s test failed

```python
if 1 == 1:
	# do something if 1 == 1 returned true
elif 2 == 2:
	# do something else if 2 == 2, but 1 == 1 returned true
```

*and*, *or*, *not* operators allow us to combine complex logical expressions:

```python
if 1 == 1 and 2 == 2 or 3 == 3:
	# do something if 1 equals 1, 2 == 2
	# do something if 3 == 3
```

Branching allows a programmer to write *linear* programs - which means that a program will always be evaluated in constant time
i.e a program will always be as long as the amount of steps in the program

___
