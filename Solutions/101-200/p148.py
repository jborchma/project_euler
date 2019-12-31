"""Solution to problem 148

I think this can be solved using Lucas theorem: https://en.wikipedia.org/wiki/Lucas%27s_theorem

Writing the binomial coefficient numbers in base 7, we should be able to count easily.

This in fact works, but it will we way too slow to scale to the billionth row. I think a better
approach will be do calculate the number of k's that will fulfill this condition based on the
number n in base 7. This should be possible to do just based on the base 7 representation without
any looping.
"""
import numpy as np

def compare_base_p(n, k, p=7):
    """compare digits
    """
    n_base_p = np.base_repr(n, base=p)
    k_base_p = np.base_repr(k, base=p)

    for i, digit in enumerate(str(k_base_p).zfill(len(str(n_base_p)))):
        if digit > str(n_base_p)[i]:
            return True

    return False


# for i in range(1, 34):
#     print(i, np.base_repr(i, base=7))

counter = 0
for n in range(400):
    n_counter = 0
    if n % 7 == 0:
        n_sum = 0
        n_sum2 = 0
    for k in range(n+1):
        if not compare_base_p(n, k):
            n_counter += 1
            counter += 1
    n_sum += n+1-n_counter
    n_sum2 += n_counter
    if (n + 1) % 7 == 0:
        print(n, np.base_repr(n, base=7), n_counter, n+1-n_counter, n_sum, n_sum2, n_sum2//7)
    else:
        print(n, np.base_repr(n, base=7), n_counter, n+1-n_counter)
print(counter)

# digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number = 340
# base = 7
# num = abs(number)
# res = []
# while num:
#     print("digit", digits[num % base])
#     res.append(digits[num % base])
#     num //= base
#     print(num)
#
# print(''.join(reversed(res or '0')))
