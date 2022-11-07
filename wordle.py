from data import data
from entropy import matches
import random


def choose_word():
    word = random.choice(data)
    return word


def get_user_input(chosen):
    word = input("Word = ").upper()
    
    if word not in data:
        if(word =="QUIT"):
            print("thanks for playing")
            return
        print("Not in word list")
        get_user_input(chosen)
        return
    res = matches(word, chosen)
    if "1" in res or "2" in res:
        print(res)
        get_user_input(chosen)
        return

    print("Got it!")
    play_again = input("Want play again? Respond with y for yes and n for no: ")
    if play_again == "y":
        chosen = choose_word()
        get_user_input(chosen)
    else:
        print("Thank you for playing!")

print("welcome to wordle, 1 means gray (the letter isn't in the word you should guess)")
print("2 means yellow (the letter is in the word you should guess but not at the right position and 3 means yellow but it is at the right position)")
print("enter \"quit\" to stop the gui")

chosen = choose_word()
get_user_input(chosen)
