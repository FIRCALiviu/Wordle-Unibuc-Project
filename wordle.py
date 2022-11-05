from data import data
from entropy import matches
import random


def choose_word():
    word = random.choice(data)
    return word


def get_user_input(chosen):
    word = input("Word = ")
    res = matches(word, chosen)

    if "1" in res or "2" in res:
        print("Wrong! Try again.")
        print(res)
        get_user_input(chosen)
        return

    print("Got it!")
    play_again = input("Wanna play again? Respond with y for yes and n for no: ")
    if play_again == "y":
        chosen = choose_word()
        get_user_input(chosen)
    else:
        print("Thank you for playing!")


chosen = choose_word()
get_user_input(chosen)
