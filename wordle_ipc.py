from data import first_dict,possibilities
import random
from multiprocessing import Process,Queue
import math

running = True
turn = True

def choose_word():
    word = random.choice(possibilities)
    return word



def gen_dict():
    aux=dict()
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
    global turn
    while running:
        while turn == True:
            pass
        
        word = q.get()

        res = matches(word, chosen)
        
        if "1" in res or "2" in res:
            q.put(res)
            print(res)
            
        else:
            print("Got it!")
            running = False
        turn = True
        return
        
        

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
    global running
    global FirstTime
    global turn
    while running:
        while turn == False:
            pass

        if FirstTime:
            q.put("TAREI")
            q.put(first_dict)
            print("TAREI")
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
            print(word_max)
        turn = False
        return
                    

def updatePossibilities(freq_dict,information):
    return freq_dict[information][1]

if __name__=='__main__':
    q = Queue()
    chosen = choose_word()
   
    p2 = Process(target=select, args=(q,))
    p1 = Process(target=get_input, args=(chosen,q,))

    p2.start()
    p1.start()
    
    p2.join()
    p1.join()
