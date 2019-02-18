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

[This problem](https://projecteuler.net/problem=85) can actually be solved most of the way by just writing out all the possible rectangles
that can be formed for a given size. Writing for each size the number of possibilities, one
can see that the overall number of squares is

sum_{i=0}^{m-1}sum_{j=0}^{n-1}(m-i)(n-j)

Executing the sums, we get

(n * (n+1) * m * (m+1)) / 4

Once we know the possible number of squares, we can just loop through the possible side lengths
and keep the best option.

### Problem 91

[This problem](https://projecteuler.net/problem=91) is very similar in context to problem  85. However, since we are now asked to find all possible triangles with a right angle that include the point (0,0) and not rectangles, this is slightly more complex.

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

### Problem 96

[The problem](https://projecteuler.net/problem=96) asks to create a solver for a Sudoku grid.
In total, there are 50 grids with varying difficulty that need to be solved.

My solution uses a mixture out of applying the simple column/row/cell based Sudoku rules as well
as guessing based on the updated grid. It works as follows:

1. Each grid is filled with either the correct integer or the set of possible integers for each
   position.
2. Once the grid is initialized, we apply the row/column/cell based rules to rule out any
   impossible numbers. In case only one number is left in the set, that number is assigned to that
   position in the grid.
3. Once we can't advance anymore with these simple rules, we start guessing a digit for each
   position based on the possible digits and then apply the rules again. Either this leads to the
   correct solution, or we move on to another guess.

This solution was able to get all 50 solutions pretty quickly.

### Problem 114

[This problem](https://projecteuler.net/problem=114) asks to calculate the number of combinations
of a number of red and black tiles with the condition that the red tiles cannot touch each other and
have a minimum length of 3.

To start I calculated the number of combinations that are possible for a given number r of red tiles
and b of black tiles. This can be found out by imagining a row of black tiles with gaps in between
them and just counting how many ways there are to place the red tiles:

```
obobobobo
```
Here `b` are black tiles and `o` are the possible spots to place the red tiles. This automatically
takes care of the rule that the red tiles cannot touch. The formula for the permutations is
`binom(b + 1, r)`, where `binom(n, k)` is the binomial coefficient.

Once I had that, I had to figure out, for a given length m, how many different combinations of
r (the number of red block) with different possible lengths there are. The fact that the red
blocks could have different lengths, made this a little harder.

I figured this out by finding the number of compositions given a specific number of red tiles r
as well as the overall length of red tiles combined (which then leaves the number of single squared
black tiles). This can be found [here](https://en.wikipedia.org/wiki/Composition_(combinatorics)#Number_of_compositions). This can be calculated by using the numpy
polynomial functionality and multiplying a correctly constructed polynomial in order to
read off the prefactor of the needed term. This is done in the `calculate_polynomial_coefficient`
function.

Now all I need to do is loop through the numbers of red tiles r starting at 1 and sum up all the
possible combinations.

### Problem 115

[The next problem](https://projecteuler.net/problem=115) is very similar to 114 and can be solved
using my solution for 114 very easily. It pretty much asks, given a minimum length `m` for the red tiles,
how long does the row need to be in order to have at least 1000000 solutions. So we can just change the
minimum length of 3 from 114 to `m` and increase the length `n` one by one to see how many combinations
we get.

### Problem 116

[This problem](https://projecteuler.net/problem=116) is much easier than the previous 2. The constraint
that the red (now also green and blue) tiles cannot touch each other is gone and also we cannot combine
special tiles of different lengths anymore. Hence, all we need to calculate is the number of
permutations for a given number of special tiles `r` and length `m` and then loop through the
possible number of special tiles for the red, green and blue lengths. The number of permutations
is given by `(r+b)!/(r! * b!) = binom(m + (1 - k) * r, r)`,
where `k` is the allowed length of the special tiles (2, 3 and 4) and m is the overall length.

### Problem 185

Coming soon

## Concepts I have used:

* Markov Chains
* Genetic Algorithms
* Monte Carlo
* Dynamic Programming
* Hidden Markov Models
