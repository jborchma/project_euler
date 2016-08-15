from random import randint as ri
from random import random as r

guesses = {"5616185650518293" : 2,
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
M = 0.06 #probability of mutation
S = len(guesses.keys().__iter__().__next__()) #string size

#creates a population of length G
populate = lambda x=None: [''.join([str(ri(0,9)) for x in range(S)]) for x in range(G)]
# calculates the fitness of the generation by checking how many guesses are fulfilled 
fitness = lambda m: sum([sum([g[x]==m[x] and 1 or 0 for x in range(S)])==guesses[g] and 1 or 0 for g in guesses]) 
# creates a new generation by taking the selected group of the previous generation, and with a probability of M creates a new number 
# or with (1-M) takes a number from a random member of the old generation. This way the full size of the population is reinstated
new_generation = lambda s: [''.join([r()<M and str(ri(0,9)) or s[ri(0,G_S-1)][k] for k in range(0,S)]) for x in range(G)]

# pop = populate()
# selected = sorted(pop,key=fitness, reverse=True)[:G_S]
# print(selected)
# new_gen = new_generation(selected)
# print(sorted(new_gen,key=fitness, reverse=True))


def main():
    high_score = 0
    population = populate()
    while high_score<len(guesses): 
        selected = sorted(population,key=fitness, reverse=True)[:G_S]
        gen_score = fitness(selected[0])
        if gen_score>high_score: 
            high_score = gen_score
            print(high_score, selected[:5])
        population = new_generation(selected)

if __name__ == "__main__":
    main()