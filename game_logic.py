from classes import Token
from constants import COUNTS, SCORES
from itertools import chain
from string import ascii_uppercase
from random import shuffle

def add_word():
    pass

def add_words():
    pass

def new_game():
    tokens = generate_tokens()
    shuffle(tokens)

def generate_tokens():
    m = map(lambda c: c * COUNTS.get(c), ascii_uppercase)
    tokens = [[Token(char, SCORES[char]) for char in letters] for letters in m]
    return list(chain.from_iterable(tokens))

print(generate_tokens())