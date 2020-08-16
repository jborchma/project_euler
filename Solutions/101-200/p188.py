"""Solution to problem 188

Python has the awesome pow method that can efficiently exponentiate numbers modulo an integer m.
However, a question that remains is: If we calculate an exponent of a number modulo m, does that
guarantee that we can calculate the next exponentiation also modulo m without losing some numbers.

The answer to that question is, at least in this case, yes (since my solution works), but I am not
fully sure I understand why this works. I think it's because 1777 and 10^8 are coprime.

One can actually derive x^(10^n) = 1 mod 10^(n+1). This means that the last n+1 digits of a^b are
determined by the last n digits of b.
"""

def T_mod(a, b, m):
    """Tetration mod m
    """
    exponent = 1
    for _ in range(b):
        new_exponent = pow(a, exponent, m)
        # if we have hit a fixed point, might not be necessary, but can speed things up
        if exponent == new_exponent:
            break
        # if we got a new exponent
        exponent = new_exponent

    return exponent

def main():
    """main function
    """
    a = 1777
    k = 1855
    m = 100000000

    print(f"The answer is: {T_mod(a, k, m)}.")


if __name__ == "__main__":
    main()
