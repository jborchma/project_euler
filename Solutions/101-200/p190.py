"""Solution to problem 190

This is a classic example of constrained optimization and can be solved via Lagrange multipliers.
Hence, for each m, we will need to solve m+1 equations (one m+1 dimensional vector equation)
and find the maximum.

This seems to be something to be done with sympy or mathematica/wolfram alpha since I need to
solve these symbolic equations.

I'll start with doing the case m=2 by hand to see if there is some sort of systematic answer.
Straightforward, one gets P2 = 32/27 and [P2] = 1 with x1=2/3 and x2=4/3.
For [P3] we get 2 with x1=2/4, x2=4/4 and x3=6/4.
But already for P4 the equations are not easy to solve... Might have to do some random search,
like Monte Carlo optimization. Luckily, the system here is pretty obvious:

x_i = 2*i/(m+1)

A way for deriving this is writing the lagrange equations as

f = prod_i x_i^i
g = m-sum_i x_i

df/dx_i = lambda dg/dx_i -> f * i/x_i = lambda -> x_i = f*i/lambda

sum_i x_i = m = f * (m+1) * m / (2 * lambda) -> f/lambda = 2/(m+1)

-> x_i = 2*i/(m+1)

Another approach is to using the inequality between the arithmetic mean >= geometric mean
with the sequence (x1, x2/2, x2/2, ..., xm/m, ...xm/m). From this, we get
Pm <= (2/(m+1))^(m*(m+1)/2) * prod_i i^i
"""

def main():
    """main function
    """
    summe = 0
    # using the mean inequality
    # for i in range(2, 16):
    #     prod = 1
    #     for j in range(1, i+1):
    #         prod *= j**j
    #     summe += int((2/(i+1))**(i*(i+1)/2) * prod)

    # using the system I discovered
    for m in range(2, 16):
        prod = 1
        for j in range(1, m+1):
            prod *= (2*j/(m+1))**j

        summe += int(prod)

    print(f"The answer is {summe}.")

if __name__ == "__main__":
    main()
