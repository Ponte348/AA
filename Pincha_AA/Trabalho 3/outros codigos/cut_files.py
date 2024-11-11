import sys

from unidecode import unidecode
import os
import random
import time
import math
random.seed(98012)

# Como vai ser corrido em dois computadores diferentes decidi implementar esta variavel para os paths
# 0 - Omen
# 1 - Asus
pc = 0

def get_paths(pc):
    if pc == 0: # OMEN
        path = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/"
        clean = path + "clean_files/"
        cutted = path+"cutted_files/"
    if pc == 1: # ASUS
        path = "D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/"
        clean = path + "clean_files/"
        cutted = path+"cutted_files/"

    return clean, cutted

def get_file_size(file):
    return os.stat(file).st_size




# Função que repete os conteudos de um ficheiro para outro N vezes
def repeat_file(clean, cuts, file_in, file_out, n):
    global size
    # Abrir o ficheiro original
    input = clean+file_in+'.txt'
    f = open(input, "r", encoding="utf8")

    # Abrir o ficheiro a ser cortado
    output = cuts+file_out+'_'+str(n)+'.txt'
    g = open(output, "w", encoding="utf8")

    # Ler o ficheiro original
    while(size < n):
        for line in f:
            for c in line:
                if c.isalpha():
                    g.write(c)
                    size += 1

    return 1


def main():
    global size

    clean, cutted = get_paths(pc)
    file_out = "time_estimation"
    file_in = "all"

    print('Size of the original file: ',get_file_size(clean+file_in+'.txt')) # 985714

    #for size_to_stop in [10**3, 10**4, 10**5, 10**6, 10**7, 10**8]:
    size_to_stop = 10**6
    size = 0
    repeat_file(clean, cutted, file_in, file_out, size_to_stop)
    print('cutted with size', get_file_size(cutted+file_out+'_'+str(size_to_stop)+'.txt'))


main()