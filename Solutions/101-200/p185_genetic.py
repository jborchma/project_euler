"""Solution to problem 185 by using a genetic algorithm.

After my first attempt of using Monte Carlo which didn't end up working in a reasonable amount of
time, I moved on and used a genetic algorithm for solving this problem. This ended up working
nicely.

For each step, I keep the best half of each generation and then use the following mutation steps:
With probablity M generate new digit or with probablity 1-M take the digit at the same position
from a random member of the old generation.
"""
from random import randint as ri
from random import random as r

GUESSES = {"5616185650518293" : 2,
           "3847439647293047" : 1,
           "5855462940810587" : 3,
           "9742855507068353" : 3,
           "4296849643607543" : 3,
           "3174248439465858" : 1,
           "4513559094146117" : 2,
           "7890971548908067" : 3,
           "8157356344118483" : 1,
           "2615250744386899" : 2,
           "8690095851526254" : 3,
           "6375711915077050" : 1,
           "6913859173121360" : 1,
           "6442889055042768" : 2,
           "2321386104303845" : 0,
           "2326509471271448" : 2,
           "5251583379644322" : 2,
           "1748270476758276" : 3,
           "4895722652190306" : 1,
           "3041631117224635" : 3,
           "1841236454324589" : 3,
           "2659862637316867" : 2}

G = 32 #the size of each generation
G_S = 16 #the size of the subset of each generation that get selected
M = 0.08 #probability of mutation, 0.06 seems to work well
S = len(GUESSES.keys().__iter__().__next__()) #string size

#creates a population of size population size
def populate(length_of_strings, population_size):
    """This function creates a population of strings for a given population size.
    """
    return [''.join([str(ri(0, 9)) for x in range(length_of_strings)]) for x in range(
        population_size)]

# calculates the fitness of the generation by checking how many guesses are fulfilled
# disabling pylint error here, since I don't edit GUESSES and this is needed as default for
# usage as key in sorted
def fitness(input_generation, length_of_strings=S, guesses=GUESSES): #pylint: disable=W0102
    """Calculate fitness

    This function calculates the fitness of each generation by counting how many
    guesses are fulfilled. It counts how many digits coincide with the known guesses. If that
    number matches the correct number of digits, it counts 1 towards the overall fitness.
    """
    return sum([sum([g[x] == input_generation[x] and 1 or 0 for x in range(length_of_strings)]
                   ) == guesses[g] and 1 or 0 for g in guesses])

def new_generation(input_generation, length_of_strings, probability_of_mutation, population_size,
                   subpopulation_size):
    """Create new, mutated generation

    This function creates a new generation by taking the selected group of the previous generation,
    and with a probability of M creates a new number
    or with (1-M) takes a number from a random member of the old generation.
    This way the full size of the population is reinstated.
    """
    return [''.join(
        [r() < probability_of_mutation and str(ri(0, 9)) #new number
         or input_generation[ri(0, subpopulation_size - 1)][k] for k in range(0, length_of_strings)]
        ) for x in range(population_size)]

def main():
    """main function that runs the algorithm
    """
    high_score = 0
    # initialize population
    population = populate(S, G)
    while high_score < len(GUESSES):
        # select best G_S members of current population
        selected = sorted(population, key=fitness, reverse=True)[:G_S]
        # score the best members with respect to the guesses
        gen_score = fitness(selected[0], S, GUESSES)
        # if the current score is the new high score, update
        if gen_score > high_score:
            high_score = gen_score
            print(high_score, selected[:5])
        # mutate population and generate new population
        population = new_generation(selected, S, M, G, G_S)

if __name__ == "__main__":
    main()
