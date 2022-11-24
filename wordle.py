from data import first_dict,possibilities
import random
from multiprocessing import Queue
import math


running=True

def choose_word():
    word = random.choice(possibilities)
    return word

def get_user_input(chosen, nr):
    word = input("Word = ")
    res = matches(word, chosen)

    userFeedback = []
    for r in res:
        if r == "1":
            userFeedback.append("GREY")
        elif r == "2":
            userFeedback.append("YELLOW")
        elif r == "3":
            userFeedback.append("GREEN")
    if ("GREY" in userFeedback) or ("YELLOW" in userFeedback):
        print(*userFeedback)
        print("Try again:")
        get_user_input(chosen, nr+1)
    else:
        print(f"Got it in {nr+1} tries! Thank you for playing")

def gen_dict():
    aux=dict()
    #we could use modulo to avoid using 5 variables, but C style loops are more efficient
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    for m in range(1,4):
                        aux[str([i,j,k,l,m])]=[0,[]]          
    return aux
    
#print(gen_dict())
def get_input(chosen,q):
    global running

    #print('getuser')
    
    
    word = q.get()

    res = matches(word, chosen)
    
    if "1" in res or "2" in res:
        q.put(res)
        print(res)
        
    else:
        print("Got it!")
        running=False
       
        

def matches(guess, chosen):
   
    output=[False for i in range(5)]
    for i in range(5):
        if guess[i] == chosen[i]:
            output[i] = 3
            
    for i in range(5):
        if not output[i]: 
            if guess[i] in chosen:    
                output[i] = 2
            else:
                output[i]=1
    
    return str(output)



def possible_matches(word_check):
    freq_dict=gen_dict()
    for word in possibilities:
        combination = matches(word_check, word)
        
        freq_dict[combination][0] += 1
        freq_dict[combination][1].append(word)
        
    aux={i:j for i,j in freq_dict.items() if freq_dict[i][0]}
    return aux

def entropy(freq_list):
    s = 0
    for i in freq_list:
        s += -i*math.log2(i)
    return s


FirstTime=True
def select(q):
    global FirstTime

    #print('select')
    
    if FirstTime:
        #print('first time')
        q.put("TAREI")
        q.put(first_dict)
        print("TAREI")
        FirstTime=False
        
    else:
        #print('not first time')
        word_max = possibilities[0]
        max_entropy = 0
        max_dict={}
        for word in possibilities:
            freq_dict=possible_matches(word)
            freq_list=[freq_dict[key][0]/len(possibilities) for key in freq_dict]
            temp=entropy(freq_list)
        
            if max_entropy < temp:
                max_entropy = temp
                word_max = word
                max_dict=freq_dict
        q.put(word_max)
        q.put(max_dict)
        print(word_max)


def updatePossibilities(freq_dict,information):
    return freq_dict[information][1]
    #print(possibilities)

if __name__=='__main__':
    #queue = Queue() print("Got it!")
    q = Queue()
    chosen = choose_word()
    user_response = input("Do you want to play by yourself? Please enter Y if so")
    if user_response == "Y":
        word_chosen = choose_word()
        get_user_input(word_chosen, 0)
    else:
        while running:
            select(q)
            get_input(chosen,q)
            if running:
                dictionar=q.get(timeout=3)
                information=q.get(timeout=3)
                possibilities=updatePossibilities(dictionar,information)
            else : break
            #print("executed a loop")
