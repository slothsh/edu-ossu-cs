# MIT 600.1 - Lecture 2

Instructor: Dr. Ana Bell

Video: Branching and Iteration

Link: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-2-branching-and-iteration/

**Classes of Algorithms**

*guess-and-check* method:

- Guess or *generate* some variable to *test* against for certain criteria
- Keep iterating and generating new guesses until the *test* passes
- This process is a part of a class of algorithms called *exhaustive enumeration* [^1]

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

[^1]: [Brute-force search - Wikipedia](https://en.wikipedia.org/wiki/Brute-force_search)
