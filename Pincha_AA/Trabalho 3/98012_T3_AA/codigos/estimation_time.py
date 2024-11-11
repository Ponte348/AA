import sys

from unidecode import unidecode
import os
import random
from time import perf_counter
import math
random.seed(98012)

# Como vai ser corrido em dois computadores diferentes decidi implementar esta variavel para os paths
# 0 - Omen
# 1 - Asus
pc = 0

def get_paths(pc):
    if pc == 0: # OMEN
        path = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/98012_T3_AA/"
        clean = path + "clean_files/"
        cutted = path+"cutted_files/"
    if pc == 1: # ASUS
        path = "D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/98012_T3_AA/"
        clean = path + "clean_files/"
        cutted = path+"cutted_files/"

    return clean, cutted

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
    print("Exact Counter: Done")
    
    return dic

def lossy_counter(e, clean,file):
    k = 1/e
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

    print("Lossy Counter: Done")

    return d

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

    print("Probabilistic Counter: Done")
    d = {key: math.floor((value / n)* 2**k) for key, value in dic_pc.items()}

    return d


def create_output_file(cutted,output):
    with open(cutted+output, "w") as f:
        f.write('Ficheiro para estimação de tempo - Gonçalo Freitas 98012\n')

    return 0

def get_file_size(file):
    return os.stat(file).st_size


# Função que repete os conteudos de um ficheiro para outro N vezes
def repeat_file(clean, cutted, file_in, file_out):
    input = clean+file_in+'.txt'
    output = cutted+file_out+'.txt'

    with open(input, "r", encoding="utf8") as f:
        with open(output, "a", encoding="utf8") as g:
                g.write(f.read())

    return 0

def cut_file(cutted, file, file_out, size_to_stop):
    # corta o ficheiro para um novo com tamanho size_to_stop
    i = 0
    with open(cutted+file+'.txt', "r", encoding="utf8") as f:
        with open(cutted+file_out+'.txt', "w", encoding="utf8") as g:
            for line in f:
                for c in line:
                    if c.isalpha():
                        g.write(c)
                        i+=1
                    if i == size_to_stop:
                        break



def main():
    global size
    clean, cutted = get_paths(pc)
    
    file = "time_estimation"
    file_in = "all" # ficheiro que vai ser repetido
    output = 'estimation_time_output.txt'

    e = 0.01
    n = 100
    k = 8

    s = get_file_size(clean+file_in+'.txt')

    max_size = 10**8
    i = 1
    # encontrar o minimo numero que multiplicado por s seja maior que max_size
    while s*i < max_size:
        i += 1
    
    # cria o ficheiro file que é o ficheiro file_in repetido i vezes
    for j in range(1,i):
        repeat_file(clean, cutted, file_in, file)


    cut = 0 # 0 - cria os ficheiros, 1- não os cria

    create_output_file(cutted,output)

    for size_to_stop in [1000, 10000, 100000, 1000000, 10000000, 100000000]:
        file_out = file+'_'+str(size_to_stop)        
        if cut == 0:
            cut_file(cutted, file, file_out, size_to_stop)
            print('Cutted with size: ',get_file_size(cutted+file_out+'.txt'),'\n')
        else:
            pass

        with open(cutted+output, "a") as f:
            f.write("\n")
            f.write("Nº of letters: "+str(size_to_stop)+"\n")

            start = perf_counter()
            dic_exact = exact_counter(cutted,file_out)
            end = perf_counter()
            exact_time = end - start
            print("time: ",exact_time," (s)\n")
            f.write("Exact counter time: "+str(exact_time)+" (s)\n")

            start = perf_counter()
            dic_prob = probabilistic_counter(n,k,cutted,file_out)
            end = perf_counter()
            prob_time = end - start
            print("time (", str(n),") : ",prob_time," (s)\n")
            f.write("Probabilistic counter time: "+str(prob_time)+" (s)\n")

            start = perf_counter()
            dic_lossy = lossy_counter(e,cutted,file_out)
            end = perf_counter()
            lossy_time = end - start
            print("time: ",lossy_time," (s)\n")
            f.write("Lossy counter time: "+str(lossy_time)+" (s)\n")

    print('Done!')


main()
