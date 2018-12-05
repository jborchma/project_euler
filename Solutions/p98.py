"""Solution to problem 98

The first thing we need to do is identify all anagram pairs in the word list.
"""
import math
import random
from collections import Counter
import itertools
from numba import jit

def is_square(number):
    """Check if a number is the square of an integer.
    """
    square_root = int(math.sqrt(number) + 0.5)
    return square_root * square_root == number

def load_words():
    """This function loads the word file into memory.
    """
    with open("p098_words.txt", "r") as file:
        for line in file:
            split_line = [word.replace('"', '') for word in line.split(",")]

    return split_line

def find_anagrams(list_of_words):
    """This function finds pairs of anagrams in a list of words.
    """
    dict_of_pairs = {}
    list_of_counts = []
    for word in list_of_words:
        list_of_counts.append(Counter(word))

    for i, count in enumerate(list_of_counts):
        for j, second_count in enumerate(list_of_counts[i+1:]):
            if count == second_count:
                dict_of_pairs[(list_of_words[i], list_of_words[i+1+j])] = (count, second_count)

    return dict_of_pairs

@jit
def find_square_pairs(pair):
    """Find square numers that are square numbers for two anagrams.
    """
    word_1 = pair[0]
    word_2 = pair[1]
    #encode words by creating mapping
    word_set = list(set(word_1))
    largest_pair = (0, 0)
    for subset in itertools.permutations(range(0, 10), len(word_set)):
        encoding = {}
        number_1 = ''
        number_2 = ''
        for letter in word_1:
            encoding[letter] = subset[word_set.index(letter)]

        for i, _ in enumerate(word_1):
            number_1 += str(encoding[word_1[i]])
            number_2 += str(encoding[word_2[i]])

        number_1 = int(number_1)
        number_2 = int(number_2)

        if is_square(number_1) and is_square(number_2):
            if (max(number_1, number_2) > max(largest_pair)
                and len(str(number_1)) == len(str(number_2))):
                largest_pair = (number_1, number_2)

    return largest_pair
#@jit
def main():
    """main function
    """
    list_of_words = load_words()
    dict_of_pairs = find_anagrams(list_of_words)
    #dict_of_pairs = {('CARE', 'RACE'):0}
    largest_number = 0
    for pair in dict_of_pairs:
        print('pair:', pair)
        number_1, number_2 = find_square_pairs(pair)
        if max(number_1, number_2) > largest_number:
            largest_number = max(number_1, number_2)
            print(largest_number)

main()
