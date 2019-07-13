"""Solution to problem 122

My approach will be to iteratively go through the numbers and calculate the lowest number of steps
that one needs to get to that exponent. I need to keep track of the list of components each number
has and then I can use them to get to the next numbers.

15: [1, 1, 3, 6, 3] is the best where the set of available numbers is {1, 2, 3, 6, 12}
15: [1, 2, 4, 4, 2, 1] is one longer, set of available numbers is {1, 2, 4, 8, 12, 14}

From this, I can see that I cannot use smaller n solutions to solve bigger ones, i.e., no
dynamic programming is possible.

So in how many jumps can I reach n, where the length of the jump can only be numbers I have
already visited.

With some googling I found: https://en.wikipedia.org/wiki/Addition_chain
which leads to https://en.wikipedia.org/wiki/Addition-chain_exponentiation
which states that the numbers we are looking for are the sequence A003313
on https://oeis.org/A003313

binary exponentiation is an upper bound for our search

I think I can solve this with iterative deepening depth-first search.
https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search

In this approach I will go from the highest possible chain with the allowed number of maximum
operations branch by branch so all other possible branches.
"""
from typing import List
import math

N_MAX = 200


def get_binary_exponentiation_bound(n):  # pylint: disable=C0103
    """get the bound of binary exponentiation

    This is the number of calculations that need to be calculated for binary exponentiation.
    The number of squarings is int(lg(n)) and the number of multiplications is the sum of the
    ones in the binary representation of n minus 1.
    """
    binary_representation = bin(n)[2:]
    n_mult = sum([1 for digit in binary_representation if digit == "1"]) - 1
    n_square = int(math.log(n, 2))

    return n_mult + n_square


class ChainTree:  # pylint: disable=R0903
    """class for search tree

    I needed to create a class in order to hold the list of already found minimum solutions
    and persist through the iterative deepening.

    Attributes
    ----------
    minimum_results: [int]
        List of known minimum solutions
    """

    def __init__(self, minimum_results: List[int]):
        self.minimum_results = minimum_results
        # self.number_of_unkown = number_of_unkown

    def traverse_tree_of_chains(self, chain, max_steps):
        """recursively traverse tree

        Parameters
        ----------
        chain: list
            This is the current addition chain we are looking at. It is effectively a stack
            where we add new values, check if we have found a better solution yet for the highest
            number in the chain and then either add more numbers, if allowed, or take out the
            number on the top and add another one.
        max_steps: int
            Number of additions allowed
        """
        # if we hit maximum length or have found all the minimum values we are looking for, end
        if len(chain) > max_steps or (
            sum([1 for number in self.minimum_results if number is None]) == 0
        ):
            return

        # traverse from left to right through the tree. The outer left branch is the branch where
        # we double the highest number up to max_steps. Then we start backtracking one node and add
        # the next highest value to the highest and then follow that branch up to max_steps
        current_maximum = chain[-1]  # use to have early stopping
        for i in reversed(range(len(chain))):
            for j in reversed(range(i + 1)):
                new_value = chain[i] + chain[j]
                if new_value <= current_maximum:
                    break  # can break since we are only looking at ascending, ordered chains
                if new_value <= N_MAX:  # if new_value is in our search range
                    chain.append(new_value)
                    # print(self.minimum_results[new_value])
                    if self.minimum_results[new_value] is None:
                        # since we are going from small number of operations to high, set value only
                        # if we haven't gotten a value yet
                        self.minimum_results[new_value] = len(chain) - 1
                        # self.number_of_unkown -= 1
                    self.traverse_tree_of_chains(chain, max_steps)
                    # when we have reached the max number of steps and have exhausted a branch,
                    # go back one step and try a new subbranch
                    chain.pop()


def main():
    """main function
    """
    minimum_operations = [0, 0] + [None] * (
        N_MAX - 1
    )  # placeholder for 0 and result for 1 is 0

    tree = ChainTree(minimum_operations)

    for num_ops in range(1, 20):
        number_of_unkown = sum([1 for number in tree.minimum_results if number is None])
        if number_of_unkown == 0:
            print("Answer:", sum(tree.minimum_results))
            break
        starting_chain = [1]  # start just with the one
        print("Starting iteration, max_ops:", num_ops)
        tree.traverse_tree_of_chains(starting_chain, num_ops)


if __name__ == "__main__":
    main()
