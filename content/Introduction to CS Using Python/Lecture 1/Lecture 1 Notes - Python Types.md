# MIT 600.1 - Lecture 1

Instructor: Dr. Ana Bell

Video: What is Computation?

Link: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-1-what-is-computation/

**A Program**
- A sequence of definitions and commands
    - definitions are a way of assigning names to values
    - creating procedures, that will be used as if they were primitives
    - commands are simpler expressions that instruct an interpreter to do
      something
- A program can be typed into a *shell* or can be stored as plain text as a
  file on disk
- A *shell* is some sort of computer interface wherein a user can input
  expressions for the computer to execute

**Fundamental Primitives**
- Programs manipulate *data objects*
- Objects have a *type* that defines the kinds of things programs can do with
  them
- A *type* tells a program what a program can do with the data
- Objects come as two types:
    - *scalars*
        - int - integers
        - floats - real numbers
        - bool - binary value; represents true or false
        - NoneType or void - special value has one value: nothing
        - In python use _type()_ function to get type of data object
    - *non-scalars*

*Type casting* tells the interpreter to take a value of a certain type and
interpret it as another type

In python the float(), str(), int(), etc
functions is used to cast types

**Expressions in Python**

Objects and operators are combined to create expressions An expression has a
value, and a value has a type To form an expression, the following simple form
is used:
- \<object\> \<operator\> \<object\> -> 1 + 2
- The value of this expression is 3, and has a type of int

*Arithmetic Operators in Python*
- \+ -> addition
- \- -> subtraction
- \* -> multiplication
- / -> division
- // -> integer division (truncates decimal part)
- % -> modulo (remainder of division)
- \*\* -> power; exponentiation

*Semantics of Python Expressions*

If both types are int, the return type is int
- int + int -> int
- int - int  -> int
- int * int -> int

If either type is int or float or both are float, the return type is float.
Python will return the 'higher-level' representation of a type when expressions
consist of mixed types
- float + float -> float
- float - float -> float
- float * float -> float
- int + float -> float
- int - float -> float
- int * float -> float

Regular division always returns a float
- int / int -> float

Integer division returns int (decimal part is truncated)
- int // int  -> int

*Operator Precedence in Python* Python obeys operator precedence - the rules
that determine which sub-expressions should be performed first in a complex
expression.

The order goes:
1. \*\*
2. \*
3. \/
4. \+ and \- (whichever appears first, left-to-right)

Parenthesis can be used to group sub-expressions to tell Python to give a
higher precedence to that expression Eg: 3 \* (3+5)
- 3 + 5 will be reduced first
- The result of the reduced expression in parenthesis will be multiplied by 3
- The return value will be 16

___
