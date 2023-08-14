# MIT 600.2 - Video: Approximate Solutions

 An approximate solution is a solution or an algorithm that does not give the *most accurate* answer to a problem,
 but it does give an answer that is it accurate enough to be considered useful.
 
 The solution is *good enough*
 A *guess-and-check* algorithm that gives an approximate solution for the cube-root of a number for an arbitrary set of numbers:
 - Start with an initial guess of a number
 - Increment it by a pre-determined small value, *epsilon*, on each new guess
- The boundaries are:

$$|guess^3| - cube \le \epsilon$$

2 issues with this approach:
1. If the *epsilon* is too large, the program won't terminate, since it will step over the correct answer
2. The program will take too long to execute of the step is too small

A good balance for *epsilon* needs to be found for a program that implements this algorithm.
The program will take:

$$ cube / \epsilon $$

steps to perform the calculation
___

### MIT 600.2 - Video: Bisection Search

*Bisection Search*, or *Binary Search*[^1] is an algorithmic strategy where a target element is searched in a sorted set of elements by continuously comparing the target to the middle-point of the set and discarding the half that does contain the target until the target is found.

The *bisection search* method is an example of an *approximate solution* algorithm.

In the square-root program, incorporating a *bisection search* algorithm allows the convergence of the correct guess to be on the order of:

$$ \log_2n $$

*Bisection search* works when value of function varies monotonically[^2] with input:
The output of the function either only grows or shrinks as the input grows or shrinks
Only works on sets/problems with a *'ordering' property*.

*Bisection search* radically reduces computation time.
___

[^1]: [Binary search algorithm - Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
[^2]: [Monotonic function - Wikipedia](https://en.wikipedia.org/wiki/Monotonic_function)
