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

def main():
    path = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/98012_T3_AA/"
    files = path + "counter/"
    tops = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/98012_T3_AA/tops/"


    lossy_dir = files + "Lossy Counter/"
    prob_dir = files + "Probabilistic Counter/"
    exact_dir = files + "Exact Counter/"

    tops_exact = tops+"exact_counter.txt"

    #joins all files in exact_dir to a file in tops_exact
    with open(tops_exact, 'w') as outfile:
        for fname in os.listdir(exact_dir):
            
            if 'metricas' in fname:
                pass
            else:
                outfile.write(fname+"\n")
                with open(exact_dir+fname) as infile:
                    for line in infile:
                        outfile.write(line)
    
    # do the same for the other counters
    tops_lossy = tops+"lossy_counter.txt"
    with open(tops_lossy, 'w') as outfile:
        for fname in os.listdir(lossy_dir):
            
            if 'metricas' in fname:
                pass
            else:
                outfile.write(fname+"\n")
                with open(lossy_dir+fname) as infile:
                    for line in infile:
                        outfile.write(line)

    tops_prob = tops+"prob_counter.txt"
    with open(tops_prob, 'w') as outfile:
        for fname in os.listdir(prob_dir):
            
            if 'metricas' in fname:
                pass
            else:
                outfile.write(fname+"\n")
                with open(prob_dir+fname) as infile:
                    for line in infile:
                        outfile.write(line)

    print('done')


main()