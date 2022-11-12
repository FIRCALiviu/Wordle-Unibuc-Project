from data import possibilities
from SolvingAgent import matches
import random
import multiprocessing
from multiprocessing import Process,Queue
from SolvingAgent import select



def choose_word():
    word = random.choice(possibilities)
    return word

# guess are valoarea TAREI initial dar
# cand intra in functia get_user_input isi pierde valoarea si 
# devine vid, de aceea word devine vid si loopeaza incontinuu pe NOt in word list
def get_user_input(chosen,q):
    word = guess.upper()
    
    if word not in possibilities:
        if(word =="QUIT"):
            print("thanks for playing")
            return
        print("Not in word list")
        get_user_input(chosen,q)
        return
    res = matches(word, chosen)
    if "1" in res or "2" in res:
        q.put(res)
        print(res)
        get_user_input(chosen,q)
        return

    print("Got it!")
    play_again = input("Want play again? Respond with y for yes and n for no: ")
    if play_again == "y":
        chosen = choose_word()
        get_user_input(chosen,q)
    else:
        print("Thank you for playing!")

print("welcome to wordle, 1 means gray (the letter isn't in the word you should guess)")
print("2 means yellow (the letter is in the word you should guess but not at the right position and 3 means yellow but it is at the right position)")
print("enter \"quit\" to stop the gui, or \"solver\" if you want the game to be solved automatically")



chosen = choose_word()
guess = ""

if __name__=='__main__':
    queue = Queue()
    p2 = Process(target=select, args=(possibilities,queue,))
    p1 = Process(target=get_user_input, args=(chosen,queue,))
    p2.start()
    p2.join()
    guess = queue.get()
    p1.start()
    p1.join()


#select:
#possibilities=freq_dict[res]