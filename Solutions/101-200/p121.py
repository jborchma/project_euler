"""Solution to problem 121

One can solve this problem exactly like problem 286 by using Markov chains.
"""
import numpy as np

# define the transition matrix
def transition_matrix(i):
    """function for creating the transition matrix
    """
    transition = np.zeros([16, 16])
    transition[range(0, 16), range(0, 16)] = i / (1+i)
    transition[range(0, 15), range(1, 16)] = 1 / (1+i)

    return transition

def main():
    """main function
    """
    probabilities = np.zeros([1, 16])
    probabilities[0, 0] = 1

    for j in range(1, 16):
        transition = transition_matrix(j)
        probabilities = np.dot(probabilities, transition)

    win_probabiltiy = 1 - sum(probabilities[0, :8])

    n = 1000 #pylint: disable=C0103

    while True:
        expecation_temp = win_probabiltiy * n - (1 - win_probabiltiy)
        if expecation_temp > 0:
            print(expecation_temp)
            print("Answer:", n)
            break
        else:
            n += 1 #pylint: disable=C0103

if __name__ == "__main__":
    main()
