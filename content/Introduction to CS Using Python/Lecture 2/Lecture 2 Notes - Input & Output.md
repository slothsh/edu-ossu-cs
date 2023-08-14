# MIT 600.1 - Lecture 2

Instructor: Dr. Ana Bell

Video: Branching and Iteration

Link: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-2-branching-and-iteration/

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

