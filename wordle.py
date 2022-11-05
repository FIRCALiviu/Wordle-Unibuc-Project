from data import data
import random


def choose_word():
    word = random.choice(data)
    return word


print(choose_word())