"""Solution to problem 78

I thought I could solve this via the solution for problem 31, but as it turns out the number we
are looking for is way too large. Hence, I think I will have to look into the partitions
and some general way to calculate the number.

Using the generalized pentagonal numbers, we can solve this with recursion.
"""
import functools

def generate_alternating_range(limit):
    """Utility function to create alternating range up to limit

    Parameters
    ----------
    limit: int
        Limit up to which the generator is created

    Yields
    ------
    int:
        Alternating sequence of integers up to limit
    """
    for i in range(1, limit + 1):
        yield i
        yield -i

def calculate_generalized_pentagonal_numbers(n): #pylint: disable=C0103
    """Calculates the first n generalized pentagonal numbers

    Parameters
    ----------
    n: int
        Integer limit up to which the numbers are generated

    Returns
    -------
    list:
        List holding the first n generalized pentagonal numbers
    """
    return [0] + [int((3 * i**2 - i) / 2)  for i in generate_alternating_range(n-1)]

@functools.lru_cache(maxsize=None)
def partitions(n): #pylint: disable=C0103
    """Calculate the number of partitions recursively

    The recursion works as follows:
    1. check if n is zero: if yes add 1 and end recursion
    2. otherwise calculate the generalized pentagonal numbers
    3. check that n> the new numbers
    4. calculate partions (n-pent number) for both the positive and the negative branch

    Parameters
    ----------
    n: int
        Number for which the number of partitions will be calculated

    Returns:
    int:
        Number of partitions
    """
    n_partition = 0
    if n == 0:
        n_partition += 1
    else:
        k = 1
        while (n >= (k * (3 * k - 1) // 2)) or (n >= (k * (3 * k + 1) // 2)):
            i = (k * (3 * k - 1) // 2)
            j = (k * (3 * k + 1) // 2)
            if (n - i) >= 0:
                n_partition += ((-1) ** (k-1)) * partitions(n - i)
            if (n - j) >= 0:
                n_partition += ((-1) ** (k-1)) * partitions(n - j)
            k += 1
    return n_partition

def main():
    """main function
    """
    for i in range(100000):
        if partitions(i) % 1000000 == 0:
            print("Answer:", i)
            break

if __name__ == "__main__":
    main()
