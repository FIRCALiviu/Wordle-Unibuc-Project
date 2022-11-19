from functools import lru_cache
from math import log2

from data import data, first_dict, possibilities


# import matplotlib.pyplot as plt


@lru_cache
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
                gray[i] = 1 # value error
    
    return str([i + j + k for i, j, k in zip(gray, yellow, green)])

@lru_cache
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


def entropy(freq_list):
    s = 0
    for i in freq_list:
        s += -i*log2(i)
    return s


def select(q):
    
    if data is not possibilities:
        word_max = possibilities[0]
        max_entropy = 0
        max_dict=None
        for word in possibilities:
            freq_dict=possible_matches(word)
            freq_list=[freq_dict[key][0]/len(possibilities) for key in freq_dict]
            temp=entropy(freq_list)
            # g.write(" ".join([word+' ',str(temp)]) + "\n")
        
            if max_entropy < temp:
                max_entropy = temp
                word_max = word
                max_dict=freq_dict
    
        q.put(word_max)
        q.put(max_dict)
    else:
        q.put("TAREI")
        q.put(first_dict)

def updatePossibilities(information,newDict):
    possibilities=newDict[information][1]



# k = possible_matches("VIASE")
# x = []
# y = []
# for key in k:
#     x.append(k[key][0])
# #    
# x.sort()
# plt.scatter(x,y)
# plt.show()
# print(possible_matches("VIASE"), sep='\n')