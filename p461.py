# use a genetic algorithm
from random import randint, random
import math

G_s = 32
G_sub = 16
p_mut = 0.16

def f(n,k):
    return math.exp(k/n) - 1

def populate():

    return [sorted([randint(1,14500) for j in range(4)]) for i in range(G_s)]

def fitness(member):
    return abs(sum([f(10000,numb) for numb in member])- math.pi)

def new_gen(gen):
    return [sorted([random() < p_mut and randint(1,14500) or member[k] for k in range(len(member))])for member in gen]

def g(member):
    return sum([numb**2 for numb in member])

best_score = 100
pop = populate()
while True:
    selected = sorted(pop,key=fitness)[:G_sub]
    gen_score = fitness(selected[0])
    if gen_score < best_score:
        best_score = gen_score
        print(best_score,selected[:3])
        print(g(selected[0]))
    pop = new_gen(selected)

