"""Solution to problem 173

if n is the length of the largest square and n is even, I can go down to n_min=4
if n is odd, I can go down to n_min=3

Now, the formula for each square with length n is 4*n-4. If we have more than one square, they need
to go in steps of two, so starting from some smallest square with length i, we have the number
of tiles for M layers of squares as sum_k 4*(i+2*k)-4, from 0 to M-1.
Doing the sum, we get 4M^2 - (8-4*i) * M. Now, all i are possible where we have
4 M^2 - (8 - 4 i) M <= N. Solving this we get i <= N/(4*M) - M + 2.

Now, all we need to do is for a given M, sum up how many integers i we have that fulfill the
inequality. (Of course I switched letters in the actual code... M -> i). Also, since we cannot have
a layer with length 1 or 2, we need to subtract 2.
"""
N = 1000000

def main():
    """main function
    """
    # i am going in steps of two
    counter = 0
    for i in range(1, N//10):
        #counter += max(0, (N+4*(i) - 2*i*(i-1))//(4*i) - 2)
        counter += max(0, N//(4*i) -i)

    print(f"Answer: {counter}.")

if __name__ == "__main__":
    main()
