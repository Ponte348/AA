from unidecode import unidecode
import os
import random
import time

random.seed(98012)

def exact_counter(clean,file):
    dic = {}
    input = clean+file+'.txt'
    with open(input, 'r') as f:
        for line in f:
            for c in line:
                if c.isalpha():
                    if c in dic.keys():
                        dic[c] += 1
                    else:
                        dic[c] = 1
        print("Exact Counter: Done - "+file)

    d = {key: value for key, value in dic.items()}
    for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True): # reverse = True - ordem decresente, reverse = False - ordem cresente 
        print("{} : {}".format(key, value))
    print("letras - ",len(dic),'\n')

    return dic

