## Importar as packages necessárias

import networkx as nX
import matplotlib.pyplot as plt
from math import floor
import random
from itertools import combinations
import time
#import numpy as np


# Função que gera o grafo com a seed do Nmec
def generate_graph(s,p):
    graph = nX.fast_gnp_random_graph(s,p,seed = 98012, directed = False)

    return graph

# Função para gerar as coordenadas de cada vértices
def coordinates(s):

    coord = [[0 for x in range(2)] for x in range(s)]

    for i in range(s):
        coord[i][0] = random.randint(0,20)
        coord[i][1] = random.randint(0,20)


    return coord


# Algoritmo Exaustivo
def exaustive(s,k,G):
    global op_exaustive
    op_exaustive = 0                                                        # Variavel para contar o nº de operações

    vert = [x for x in range(s)]                                            # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]

    Length = floor(s*k)

    list_combinations = []                                                  # Vamos ver todas as combinações possíveis
    for n in range(len(vert) + 1):                                          # Pondo tudo dentro deste for torna-se mais rapidos pois não se guarda todas as combinações possiveis, o que para grafos grandes tornava-se bastante dispendioso
        for comb in combinations(vert, n):
            list_combinations.append(comb)

        n_comb = len(list_combinations)

        for a in range(n_comb):
            S = list(list_combinations[a])                                  # vai iterando e vendo a combinação
            result =  [0 for x in range(s)]
            for c in range(len(vert)):
                check = vert[c]                                             # vai iterando e vendo o vertice
                K = list(G.neighbors(check))
                op_exaustive = op_exaustive + 1                             # Para contar o número de operações -> dentro do for mais interior
                if check not in S:                                          # Definição de set dominante -> Todo o vertice não em S
                    if any(i in K for i in S):                              # É adjacente a pelo menos 1 vertice em S
                        result[c] = 1
                    else:
                        result[c] = -1                                      # Para invalidar os sets

            if -1 not in result:                                            # Se o set é válido pode retornar
                return S

    return []                                                               # Se chegar ao fim e não encontrar retorna o conjunto vazio

def main():
    global op_exaustive
    global op_heuristic

    P_list = [0.125]
    K = [0.125,0.25,0.5,0.75]
    S = [x for x in range(4,26)]
    #P_list = [0.5]
    #K = [0.75]
    #S = [5]


    for z in range(len(P_list)):
        P = P_list[z]

        for r in range(len(K)):

            e_time = [0 for x in range(len(S))]                         # Tempo Exaustiva
            e_op = [0 for x in range(len(S))]                           # Operações Exaustiva

            for w in range(len(S)):
                s = S[w]
                k = K[r]
                
                #coord = coordinates(s)

                print("\nN vertice:",s, "\nk = ", k,"\nP =",P)
                print("Comprimento do dominating set tem que ser:", floor(s*k))

                G = generate_graph(s,P)
                print("Dominating set:")
                print(nX.dominating_set(G))

                tic = time.perf_counter()

                G = generate_graph(s,P)
                S_E = exaustive(s,k,G)
                print("\nExaustive Result:",set(S_E))
                toc = time.perf_counter()
                e_time[w] = toc-tic
                e_op[w] = op_exaustive
                print(f"Time: {toc - tic:0.4f} seconds")


                if len(S_E) != 0:
                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))

        
            print("Times Exaustive:", e_time)

            print("Operações Exaustive:", e_op)

            with open("D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 1/ALL_4_25.txt","a") as f:
                f.write("\n"+"Size ="+str(S)+"; %K ="+str(k)+"; %P ="+str(P)+";")
                f.write("\n"+"Op_Exaustive ="+ str(e_op)+";")
                f.write("\n"+"Times_Exaustive ="+ str(e_time)+";")
                f.write("\n")

        #f.close()
    



if __name__ == "__main__":
   main()


