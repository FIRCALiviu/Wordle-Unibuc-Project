from data import first_dict,possibilities,data
import random
from multiprocessing import Queue
import math


running=True

def choose_word():
    word = random.choice(possibilities)
    return word



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

def get_input(chosen,q):
    global running

    
    word = q.get()

    res = matches(word, chosen)
    
    if "1" in res or "2" in res:
        q.put(res)
  
        
    else:

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
    global FirstTime,session

   
    if FirstTime:
   
        q.put("TAREI")
        q.put(first_dict)
        session+=' TAREI'
        FirstTime=False
        
    else:
    
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
        session+=' {}'.format(word_max)
                    

def updatePossibilities(freq_dict,information):
    return freq_dict[information][1]
    #print(possibilities)


if __name__=="__main__":
    with open('solutions.txt','w') as file:
        for word in data:
            session=word
            possibilities=data
            FirstTime=True
            running=True
            q = Queue()

            while running:
                select(q)
                get_input(word,q)
                if running:
                    dictionar=q.get(timeout=3)
                    information=q.get(timeout=3)
                    possibilities=updatePossibilities(dictionar,information)
                else : break
            file.write('\n'+session)
