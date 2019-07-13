"""Monte Carlo approach to problem 185

In this approach I will use a stochastic approach that will try the most probable guess for
each digit first and then move on to lower ones. It turned out not to work in a reasonable amount
of time, so I moved on to a genetic algorithm.
"""
import random
import time
import numpy

start = time.time()

# input_dict = {90342: 2, 70794 : 0, 39458 : 2, 34109 : 1, 51545 : 2, 12531 : 1}
# NUMBER_LENGTH = 5

GUESSES = {
    "5616185650518293": 2,
    "3847439647293047": 1,
    "5855462940810587": 3,
    "9742855507068353": 3,
    "4296849643607543": 3,
    "3174248439465858": 1,
    "4513559094146117": 2,
    "7890971548908067": 3,
    "8157356344118483": 1,
    "2615250744386899": 2,
    "8690095851526254": 3,
    "6375711915077050": 1,
    "6913859173121360": 1,
    "6442889055042768": 2,
    "2321386104303845": 0,
    "2326509471271448": 2,
    "5251583379644322": 2,
    "1748270476758276": 3,
    "4895722652190306": 1,
    "3041631117224635": 3,
    "1841236454324589": 3,
    "2659862637316867": 2,
}

NUMBER_LENGTH = 16

# this does not work!
def check():
    guesses = {i: [] for i in range(NUMBER_LENGTH)}
    for i in range(100):
        summe = 0
        liste = []
        while summe < 17:
            number = random.choice(list(GUESSES.keys()))
            summe += GUESSES[number]
            liste.append(number)

        if summe == 17:
            for i in range(NUMBER_LENGTH):
                ints = [str(number)[i] for number in liste]

                guesses[i].extend(list(set([x for x in ints if ints.count(x) > 1])))

    guesses_set = {i: list(set(guesses[i])) for i in range(NUMBER_LENGTH)}

    for number in GUESSES:
        if GUESSES[number] == 0:
            for i, digit in enumerate(str(number)):

                guesses_set[i].remove(digit)

    print([len(guesses_set[i]) for i in range(NUMBER_LENGTH)])


# now we create the probability tables for each position
def check_guess(n):
    for number in GUESSES.keys():
        count = 0
        for i in range(len(str(n))):
            if str(n)[i] == str(number)[i]:
                count += 1

        if count != GUESSES[number]:
            return False

    return True


def metric(n):
    distance = 0
    for number in GUESSES.keys():
        count = len([1 for i in range(len(str(n))) if str(n)[i] == str(number)[i]])
        distance += (count - GUESSES[number]) ** 2

    return distance


# the key is the position of the digit and the list will be filled with the probabilities for each number in order 0-9
probability_dict = {
    i: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] for i in range(NUMBER_LENGTH)
}

# if a number is ruled out, we set the probability to -1, in order to distinguish from the case where we have no information
for number in GUESSES.keys():
    correct_count = GUESSES[number]
    if correct_count > 0:
        for i, digit in enumerate(str(number)):
            if probability_dict[i][int(digit)] >= 0:
                probability_dict[i][int(digit)] += correct_count / NUMBER_LENGTH
    else:
        for i, digit in enumerate(str(number)):
            probability_dict[i][int(digit)] = 0


possibilities = {i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(NUMBER_LENGTH)}
for number in GUESSES.keys():
    correct_count = GUESSES[number]
    if correct_count == 0:
        for i, digit in enumerate(str(number)):
            possibilities[i][int(digit)] = 0


# # after we have created the sums of the probabilities we now will guess through the possible combinations and check against all the guesses


def random_guess():
    guess = []
    for i in range(NUMBER_LENGTH):
        len_poss = len(possibilities[i])
        rand = random.randint(0, len_poss - 1)
        guess.append(str(possibilities[i][rand]))

    return "".join(guess)


# norm_prob = {  i : numpy.ndarray.tolist(numpy.array(probability_dict[i])*1/sum(probability_dict[i])) for i in range(NUMBER_LENGTH)  }

initial_guess = random_guess()
old_metric = metric(int(initial_guess))
number = list(initial_guess)
print(initial_guess, old_metric)

len_poss = len(possibilities[0])

track = numpy.zeros([2])
helper = 0
k = 1
restarts = 0
while True:
    # define random digit and copy number to temp
    digit = random.randint(0, NUMBER_LENGTH - 1)
    temp_list = number[
        :
    ]  # I need to use the slice! If I use just temp_list = number it'll only create a reference!!!!
    rand = random.randint(0, len_poss - 1)

    # switch this digit in temp for the random one
    temp_list[digit] = str(possibilities[digit][rand])
    # measure new version and if it is an improvement, reset number to new value
    new_metric = metric(int("".join(temp_list)))
    if new_metric < old_metric:
        number = list("".join(temp_list))
        old_metric = new_metric
    elif old_metric - new_metric:
        T = 1 / numpy.log((k + 10) / 10)
        choice = numpy.random.choice(
            numpy.arange(0, 2),
            p=[
                1 - numpy.exp(-(new_metric - old_metric) / T),
                numpy.exp(-(new_metric - old_metric) / T),
            ],
        )
        if choice == 1:
            number = list("".join(temp_list))
            old_metric = new_metric

    if metric(int("".join(number))) == 0:
        print(int("".join(number)))
        print("Number found...")
        break
    if k % 400 == 0:
        helper = (helper + 1) % 2
        track[helper] = metric(int("".join(number)))
        if track[helper] == track[helper - 1]:
            new_guess = random_guess()
            old_metric = metric(int(new_guess))
            number = list(new_guess)
            track = numpy.zeros([2])
            restarts += 1
            if restarts % 20 == 0:
                print("Restarts: ", restarts)
            k = 1
    k += 1

# maybe it would be cool to accept non-optimal solutions with a non-vanishing probability along the lines of exp(-(new_metric - old_metric)/T) for some T.
# T could slowly decrease and thus "freeze out" the algorithm


# #check most probable manually
# number = ''
# for i in range(NUMBER_LENGTH):
#     digit = probability_dict[i].index(max(probability_dict[i]))
#     number = number + str(digit)

# # if I found the number, print number
# if check_guess(int(number)):
#     print('The number is %s' % number)
# # now I need to find the next best guess
# else:
#     while status:
#         new_number = ''
#         for i in range(NUMBER_LENGTH):
#             new_number += str(numpy.random.choice(numpy.arange(0, 10), p=norm_prob[i]) )
#         if check_guess(int(new_number)):
#             print('The number is %s' % new_number)
#             status = False


print("The calculation took %s s." % (time.time() - start))
