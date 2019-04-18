"""Solution to problem 180

Doing some algebra, f_n = (x + y + z) * (x^n + y^n - z^n)

So, any zero will have x^n + y^n = z^n. Thanks for Fermat's theorem, we know only n=1 and n=2
can possibly have rational solutions (plus the negative -1 and -2).

The tricky part is to calculate the n'th root of the fraction properly.
"""
from fractions import Fraction
import math

def find_zero(n, order): #pylint: disable=C0103
    """Finds zeros for Fermat's equation
    """
    if n > 2:
        raise Exception(f"No solutions exist for order {n}.")

    list_of_zeros = []
    # find all possible candidates
    fraction_set = set(Fraction(a, b) for b in range(order + 1) for a in range(1, b))

    for x in fraction_set: #pylint: disable=C0103
        for y in fraction_set: #pylint: disable=C0103
            if x > y:
                continue
            z_n = (x**n + y**n)
            z = take_fraction_root(z_n, n) #pylint: disable=C0103
            if z in fraction_set:
                list_of_zeros.append((x, y, z))

    return list(set(list_of_zeros))

def take_fraction_root(z, power): #pylint: disable=C0103
    """Function to take the root to the power'th power

    Parameters
    ----------
    z: fraction.Fraction
        Fraction of which the root will be taken
    power: int
        Power to which the root is taken

    Returns
    -------
    fraction.Fraction
        The calculated power'th root of the input fraction.
    """
    if power < 0:
        # if negative exponent, flip over
        return take_fraction_root(1 / z, -power)
    a, b = z.numerator, z.denominator #pylint: disable=C0103
    power_a = int(math.pow(a + 0.1, 1 / power))
    power_b = int(math.pow(b + 0.1, 1 / power))
    if power_a > 0 and power_b > 0 and Fraction(power_a, power_b)**power == z:
        return Fraction(power_a, power_b)
    return 0

def main():
    """main function
    """
    full_s_list = []
    for power in [1, 2, -2, -1]:
        test = find_zero(power, 35)
        full_s_list += list(sum(zero) for zero in test)

    full_s_list = list(set(full_s_list))
    summe = sum(full_s_list)

    print("Answer:", summe.numerator + summe.denominator)

if __name__ == "__main__":
    main()
