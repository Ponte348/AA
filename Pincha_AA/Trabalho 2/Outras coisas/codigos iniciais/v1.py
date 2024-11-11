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


# Algoritmo
def exaustive(s,K,G):
    global op_exaustive
    global N_conf_E
    N_conf_E = 0                                                            # Variavel para contar o nº de Configurações
    op_exaustive = 0                                                        # Variavel para contar o nº de operações

    vert = [x for x in range(s)]                                            # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]

    Length = K

    list_combinations = []                                                  # Vamos ver todas as combinações possíveis
    for n in range(len(vert) + 1):                                          # Pondo tudo dentro deste for torna-se mais rapidos pois não se guarda todas as combinações possiveis, o que para grafos grandes tornava-se bastante dispendioso
        for comb in combinations(vert, n):
            if len(comb) == Length:                                         # Apenas queremos as combinações com o tamanho pretendido
                list_combinations.append(comb)

    n_comb = len(list_combinations)

    for a in range(n_comb):
        N_conf_E = N_conf_E + 1

        if N_conf_E == 10:
            break

        S = list(list_combinations[a])                                  # Vai iterando e vendo a combinação
        result =  [0 for x in range(s)]
        for c in range(len(vert)):
            check = vert[c]                                             # Vai iterando e vendo o vertice
            K = list(G.neighbors(check))
            op_exaustive = op_exaustive + 1                             # Para contar o número de operações -> dentro do for mais interior
            if check not in S:                                          # Definição de set dominante -> Todo o vertice não em S
                if any(i in K for i in S):                              # É adjacente a pelo menos 1 vertice em S
                    result[c] = 1
                else:
                    result[c] = -1                                      # Para invalidar os sets

        if -1 not in result:                                            # Se o set é válido pode retornar e parar a execução
            return S

    return []                                                               # Se chegar ao fim e não encontrar retorna o conjunto vazio

def main():
    global op_exaustive                                                     # Contador do número de operação básicas para o Algortimo Exaustivo
    global Total_Tested


    P_list = [0.125,0.25,0.5,0.75]                                          # Dado duas arestas P corresponde a probabilidade de ela existir, serve para tornar os grafos mais/menos densos
    S = [x for x in range(4,10)]                                            # Tamanho do grafo


    for z in range(len(P_list)):
        P = P_list[z]
        print("\nP =",P)

        e_time = [0 for x in range(len(S))]                             # Tempo 
        e_op = [0 for x in range(len(S))]                               # Operações 
        n_solutions_E = [0 for x in range(len(S))]                      # Nº Soluções
        n_config_E = [0 for x in range(len(S))]                         # Nº Configurações
        k_vector = [0 for x in range(len(S))]
        solutions = [0 for x in range(len(S))]

        for w in range(len(S)):
            s = S[w]
            print("\nN vertice:",s)

            op_best = 100000000

                
                
            #coord = coordinates(s)                                      # Gerar coordenadas dos vértices

            tamanhos = []
            Total_Tested = 1

            while(Total_Tested <= 10):

                K = random.randint(1,s-1)

                while(K in tamanhos):
                    K = random.randint(1,s-1)


                tamanhos.append(K)

                print("\nK = ", K, "( Tentativa :", Total_Tested,")")
                print("Comprimento do dominating set tem que ser:", K)

                G = generate_graph(s,P)
                print("Dominating set:")
                print(nX.dominating_set(G))


                tic = time.perf_counter()


                S_E = exaustive(s,K,G)
                #print("\nExaustive Result:",set(S_E))
                toc = time.perf_counter()
                if len(S_E) != 0:
                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))
                    if op_exaustive < op_best:
                        e_time[w] = toc-tic
                        e_op[w] = op_exaustive
                        n_config_E[w] = N_conf_E
                        k_vector[w] = K
                        n_solutions_E[w] = 1
                        solutions[w] = set(S_E)
                else:
                    print("No result") 
                            

                print(f"Time: {toc - tic:0.4f} seconds")

                Total_Tested += 1

        print("Best Operações:", e_op)
        print("Times:", e_time)
        print("Configurações: ", n_config_E)
        print("Ks:", k_vector)
        print("Solutions:", solutions)


        with open("C:/Users/OMEN/Desktop/Output_98012.txt","a") as f:
            f.write("\n"+"Size ="+str(S)+"; P ="+str(P)+";")
            f.write("\n"+"Ks ="+ str(k_vector)+";")
            f.write("\n"+"Operações ="+ str(e_op)+";")
            f.write("\n"+"Tempo ="+ str(e_time)+";")
            f.write("\n"+"N_Solutions ="+ str(n_solutions_E)+";")
            f.write("\n"+"N_Configurations ="+ str(n_config_E)+";")
            f.write("\n"+"Solutions ="+ str(solutions)+";")
            f.write("\n")

            #f.close()
    



if __name__ == "__main__":
   main()


