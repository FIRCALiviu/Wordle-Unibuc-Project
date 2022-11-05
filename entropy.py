from data import data
import math
# import matplotlib.pyplot as plt



def matches(guess, chosen):
    copy = list(chosen)
    green = [0, 0, 0, 0, 0]
    yellow = [0, 0, 0, 0, 0]
    gray = [0, 0, 0, 0, 0]
    for i in range(5):
        if guess[i] == chosen[i]:
            green[i] = 1
            copy.remove(guess[i])
    for i in range(5):
        if guess[i] in copy :
            yellow[i] = 1
            copy.remove(guess[i])  # value error
        else:
            gray[i] = 1
    
    return str([i + j*2 + k * 3 for i, j, k in zip(gray, yellow, green)])


def possible_matches(word_check):
    global data
    freq_dict = dict()
    for word in data:
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
        s += -i*math.log2(i)
    return s


def select():
    
    
    word_max = data[0]
    max_entropy = 0
    
    for word in data:
        freq_dict=possible_matches(word)
        freq_list=[freq_dict[key][0]/len(data) for key in freq_dict]
        temp=entropy(freq_list)
        # g.write(" ".join([word+' ',str(temp)]) + "\n")
      
        if max_entropy < temp:
            max_entropy = temp
            word_max = word
    return word_max



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