from data import data
from wordle import matches,choose_word
import os
from termcolor import colored

def get_user_input(chosen):
    word = input("Word: ").upper()
    if word not in data:
        if(word =="QUIT"):
            print("thanks for playing")
            return
        print("Not in word list")
        get_user_input(chosen)
        return
    res = matches(word, chosen)
    if "1" in res or "2" in res:
        for i in [1,4,7,10,13]:
            if res[i] == '1':
                print(colored(word[i//3],'red'),end="")
            if res[i] == '2':
                print(colored(word[i//3],'yellow'),end="")
            if res[i] == '3':
                print(colored(word[i//3],'green'),end="")
        print()
        get_user_input(chosen)
        return
    print("Got it!")
    play_again = input("Want play again? Respond with y for yes and n for no: ")
    if play_again == "y":
        chosen = choose_word()
        get_user_input(chosen)
    else:
        print("Thank you for playing!")

print("welcome to wordle, if you want to play type y, else if you would like to let the computer solve the puzzle type anything else")
print("enter \"quit\" to stop the gui")


def wordle():
    chosen = choose_word()
    get_user_input(chosen)

def main():
    verif = True
    ch = input("Response: ").lower()
    if ch == "y":
        verif = False
        wordle()
    else:
        os.system('python wordle_ipc.py')
main()
