from data import data,possibilities
from SolvingAgent import matches,select,updatePossibilities
from random import choice
from multiprocessing import Process,Queue
running=True

def choose_word():
    word = choice(data)
    return word


def get_user_input(chosen,q):
    word = q.get().upper()
    

    res = matches(word, chosen)
    if "1" in res or "2" in res:
        print(res)
        q.put(res)
        return

    print("Got it!")
    play_again = input("Want to play again? Respond with y for yes and n for no: ")
    if play_again == "y":
        chosen = choose_word()
        possibiliies=data
        get_user_input(chosen)
    else:
        global runnig
        runnig=False

#print("welcome to wordle, 1 means gray (the letter isn't in the word you should guess)")
#print("2 means yellow (the letter is in the word you should guess but not at the right position and 3 means yellow but it is at the right position)")
#print("enter \"quit\" to stop the gui")

chosen = choose_word()


if __name__=="__main__":
    q=Queue()
    information=None
    chosenDict=None
    p1=Process(target=select,args=(q,))
    p2=Process(target=get_user_input, args=(chosen,))
    p3=Process(target=updatePossibilities,args=(information,chosenDict,))
    while running:
        p1.start()
        p1.join()
        p2.start()
        p2.join()
       
        chosenDict=q.get()
        information=q.get()
        p3.start()
        p3.join()
        
