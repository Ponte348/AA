from unidecode import unidecode
import os
import random
import time
import math

random.seed(98012)

def lossy_counter(e, clean,file):
    k = math.ceil(1/e)
    n = 0
    i = 1
    dic ={}

    input = clean+file+'.txt'

    with open(input, "r", encoding="utf8") as f:
        for line in f:
            for c in line:
                if c.isalpha():
                    n +=1
                    if c not in dic.keys():
                        # cria nova entrada no dicionario com (1, i-1), i.e, (contador, delta)
                        dic[c] = [1, i-1]
                    else:
                        # se já existe no dicionario incrementa-se se o contador e não se atualiza o valor do delta
                        dic[c][0] += 1      # contador
                    
                    if n == k:
                        for key in list(dic.keys()):
                            if dic[key][0] + dic[key][1] < i:
                                del dic[key]
                        i += 1
                        n=0
                        

    d = {key: value for key, value in dic.items()}
    for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True): # reverse = True - ordem decresente, reverse = False - ordem cresente 
        print("{} : {}".format(key, value[0]))
    print("letras - ",len(dic),'\n')



    return d