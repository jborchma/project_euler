from scipy.special import binom

counter = 0
for n in range(23, 101):
    for k in range(3, n - 1):
        if binom(n, k) >= 1000000:
            counter += 1

print(counter)
