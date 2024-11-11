from unidecode import unidecode
import os
import random
import time
import math

random.seed(98012)

def increment_counter(prob=0.5):
    if random.random() < prob:
        return 1

    return 0


def probabilistic_counter(n,k,clean,file):
    input = clean+file+'.txt'
    dic_pc ={}
    for i in range(n):
        with open(input, 'r') as f:    
            for line in f:
                for c in line:
                    if c.isalpha():
                        if c in dic_pc.keys():
                            dic_pc[c] += increment_counter(1/2**k)
                        else:
                            dic_pc[c] = 1

    print("Probabilistic Counter: Done - "+file)
    d = {key: math.floor((value / n)* 2**k) for key, value in dic_pc.items()}
    for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True): # reverse = True - ordem decresente, reverse = False - ordem cresente 
        print("{} : {}".format(key, value))
    print("letras - ",len(d),'\n')

    return d


