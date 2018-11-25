# project_euler

Here I upload some of my solutions to Project Euler problems using Python. Most of them are from myself, some of them are done using hints.

## Incomplete list of my favourite problems

So far, my documentation about my solutions has been rather scarce, so my plan is to improve this
moving forward. One reason is that it has been quite a long time since I have worked on many of
these problems and I have probably forgotten a lot about how I solved some of the problems.
The second reasons is that for anybody except me it must be even harder to follow what I did.
I am starting by adding small write ups for some of my favourite problems to this README as a
first attempt to be more clear about my solutions.

### Problem 85

This problem can actually be solved most of the way by just writing out all the possible rectangles
that can be formed for a given size. Writing for each size the number of possibilities, one
can see that the overall number of squares is

sum_{i=0}^{m-1}sum_{j=0}^{n-1}(m-i)(n-j)

Executing the sums, we get

(n * (n+1) * m * (m+1)) / 4

Once we know the possible number of squares, we can just loop through the possible side lengths
and keep the best option.

### Problem 91

[This problem](https://projecteuler.net/problem=91) is very similar in context to problem  85. However, since we are now asked to find all possible triangles with a right angle that include the point (0,0) and not rectangles, this is
slightly more complex.

This means we can use Pythagoras' theorem to set up equations for the triangles. In total, there
are three possibilities: the hypothenuse could be either of the sides 0->1, 1->2 or 2->0. From
this, we get:

1. x_1 * x_2 + y_1 * y_2 = 0
2. x_1 * (x_1 - x_2) + y_1 * (y_1 - y_2) = 0
3. x_2 * (x_2 - x_1) + y_2 * (y_2 - y_1) = 0

Since the problem only asks for N=50, we can now just loop through all possible combinations
to get all possible solutions. For higher numbers, one could further solve these equations
and manually count all possible solutions. One important thing to keep in mind is that we only
count distinct triangles.

### Problem 185

Coming soon

## Concepts I have used:

* Markov Chains
* Genetic Algorithms
* Monte Carlo
* Dynamic Programming
* Hidden Markov Models
