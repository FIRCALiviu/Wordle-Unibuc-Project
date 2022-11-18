from data import first_dict,possibilities
import random
from multiprocessing import Process, Queue
import math

# functia de alegere a cuvantului random 
def choose_word():
    word = random.choice(possibilities)
    return word

#running pentru a iesi din while ul infinit atunci cand functia matches() returneaza [3,3,3,3,3] (adica cuvantul a fost ghicit)
running=True
#last_word pentru a verifica daca item ul extras din queue este diferit de cel nou
last_word = ""
#functia get_user_input face legatura intre wordle si programul care rezolva
def get_user_input(chosen,q):
    global running,last_word
    while running:
        word = q.get()
        if word != last_word and len(last_word)!=0:
            combination=q.get()
            res = matches(word, chosen)
            updatePossibilities(res,combination)
            if "1" in res or "2" in res:
                q.put(res)
                print(res)
            else:
                print("Got it!")
                running=False
                break
        last_word = word
        
#functia matches() returneaza informatia cuvantului ales 1 pentru litera gri, 2 pentru galbel si 3 pentru verde
def matches(guess, chosen):
    green = [0, 0, 0, 0, 0]
    yellow = [0, 0, 0, 0, 0]
    gray = [0, 0, 0, 0, 0]
    for i in range(5):
        if guess[i] == chosen[i]:
            green[i] = 3
            
    for i in range(5):
        if not green[i]: 
            if guess[i] in chosen:    
                yellow[i] = 2
            else:
                gray[i]=1
    
    return str([i + j + k for i, j, k in zip(gray, yellow, green)])

#functia possible_matches() returneaza in dictionarul freq_dict ca si cheie combinatia si ca si valoare frecventa combinatiei si cuvintele care ofera acea combinatie
def possible_matches(word_check):
    freq_dict = dict()
    for word in possibilities:
        combination = matches(word_check, word)
        if combination in freq_dict:
            freq_dict[combination][0] += 1
            freq_dict[combination][1].append(word)
        else:
            freq_dict[combination] = [1, [word]]
    return freq_dict

#functia entropy() calculeaza entropia
def entropy(freq_list):
    s = 0
    for i in freq_list:
        s += -i*math.log2(i)
    return s

#FirstTime pentru a pune primul cuvant TAREI altfel calculeaza pe baza rezultatului oferit cuvantul cu entropia cea mai mare
FirstTime=True
#last_res pentru a verifica daca ultimul item extras din queue e diferit de cel nou
last_res = []
#functia select() selecteaza cuvantul cu cea mai mare entropie
def select(possibilities,q):
    global FirstTime,last_res
    while  running:
        if FirstTime:
            q.put("TAREI")
            q.put(first_dict)
            print("TAREI")
            FirstTime=False
        else:
            res = q.get()
            if res != last_res and len(last_res)!=0:
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
            last_res = res

#functia updatePossibilites pune taie cuvintele care nu ne mai ofera informatie din lista
def updatePossibilities(res,freq_dict):
    possibilities = freq_dict[res][1]

#definirea queue ul a proceselor si startul lor
if __name__=='__main__':
    q = Queue()
    chosen = choose_word()
    p2 = Process(target=select, args=(possibilities,q))
    p2.start()
    p1 = Process(target=get_user_input, args=(chosen,q))
    p1.start()
    p2.join()
    p1.join()

