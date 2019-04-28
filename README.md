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

### Problem 117

[This problem](https://projecteuler.net/problem=116) is similar to 116, but now the calculation of the permutations is

```
(r + g + b + s)!/(r!g!b!s!) = (m - r - 2*g - 3*b)!/(r!g!b!*(m - 2*r - 3*g - 4*b)!)
```

Now we just need to loop through all possible combinations of r, g and b.

### Problem 124

[This problem](https://projecteuler.net/problem=124) was decently easy as it built upon prime
factorization where I could reuse my function from problem 69, for example.

Effectively it worked in the following way:

1. factorize each number
2. calculate the radical and save in a dictionary
3. sort dictionary by value
4. read of the 9999th item

### Problem 125

I thought [this problem](https://projecteuler.net/problem=125) was very interesting. The task was
to find all numbers below 10^8 that are palindromic and are the sums of at least two consecutive
square numbers.

The algorithm I used to search through all palindromes was the following:

1. We initialize the upper and lower bound to 1
2. We calculate the maximum number possible (the square root of our N_MAX
3. initialize sum as 1
4. ----- WHILE LOOP ------ (as long as the sum is not equal the input number)
  1. if the sum is smaller than the number:
     add the square of the upper bound to the sum and increase the upper bound by 1
  2. elif the sum is larger than the number:
     subtract the square of the lower bound and increase lower bound by 1

  3. if now the upper bound is larger than the maximum number:
       the number is not a sum of consecutive square numbers
   ----- END OF WHILE LOOP -----

5. if the upper bound is larger than the lower bound:
the number is the sum of at least two consecutive square numbers
(if upper_bound = lower_bound it would be only one square number)

The trick to finding all palindromic numbers was to construct them as opposed to searching for them.
This could be done by using the numbers as string (so that it would keep leading 0s) and then once
we had all possible numbers up to the maximum, we would filter out the leading 0 numbers and dedupe.

### Problem 127

When I started [this problem](https://projecteuler.net/problem=125), I thought I would be able to
just use my solution from 125 and do some optimized brute force search. However, as it turns out,
the search space for this problem was way too large to go about this in this way. Instead, I used
a really cool trick: use the sieve of Eratosthenes that is normally used for finding primes up to
a limit to also find all radicals up to a limit. This works, since we need to find all prime
factors or a given number n to find its radical, so instead of ruling out numbers that are multiples
of a prime, we note the number itself and in the end get the radical:

```python
def radical_sieve(limit):
    """Function that creates a list of radicals based on the sieve of Eratosthenes

    Parameters
    ----------
    limit: int
        Limit for the sieve. Up to this number, all radicals will be calculated

    Returns
    -------
    list:
        List holding the radicals for number n at index n
    """
    radical_list = [1] * (limit + 1)
    radical_list[0] = 0
    for i in range(2, len(result)):
        if radical_list[i] == 1:
            for j in range(i, len(result), i):
                radical_list[j] *= i
    return radical_list
```

### Problem 134

This is actually a pretty simple problem, conceptually. But as always, using the straightforward
way will take way too long (at least with Python). So I actually had to think about this and do some
math. Along the way I learned about modular inverse and how to calculate it.

We are looking for a number n = i * 10**(digits_1) + prime_1 and n mod prime_2 = 0. We can solve
this equation like any normal equation, but we have to keep in mind that when dividing by a number
in a modular equation we have to use the modular inverse, not just the normal inverse. Doing the
math, we get i = -prime_1 * (10**(digits))^(-1) % prime_2, where (10**(digits))^(-1) is the modular
inverse. This combined with the fast prime sieve I've been using solves the problem pretty quickly.

### Problem 185

Coming soon

## Concepts I have used:

* Markov Chains
* Genetic Algorithms
* Monte Carlo
* Dynamic Programming
* Hidden Markov Models
