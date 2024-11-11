## Importar as packages necessárias

import networkx as nX
import matplotlib.pyplot as plt
import math
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
# Algoritmo
def exaustive(Size,n,usr_perc,G):
        global op_exaustive
        global N_conf_E
    
        N_conf_E = 1                                                            # Variavel para contar o nº de Configurações

        op_exaustive = 0                                                        # Variavel para contar o nº de operações
        
        number_of_combinations = math.factorial(Size)/(math.factorial(n)*math.factorial(Size-n))        # Número total possivel de combinações de tamanho n com Size vertices

        if type(usr_perc) is float:
            k = math.ceil(number_of_combinations*usr_perc)                      # Apenas queremos x % dessas combinações para análise
        else:
            k = min(number_of_combinations,usr_perc)                            

        print("\nGonna Analyze",int(k),"combinations")

        to_test = list(random.sample(range(int(number_of_combinations)),int(k)))     # Gera k números random correspondestes ao número da combinações para analise, p.ex. 1-> combinação nº1
        

        testing = 0

        vert = [x for x in range(Size)]

        for S in combinations(vert, n):                                             # Itera em todas as combinações
            if testing in to_test:                                                  # Caso seja uma que se pretende analisar
                N_conf_E = N_conf_E + 1                                             # Incrementa o número de configurações analisadas
                result =  [0 for x in range(Size)]
                for c in range(len(vert)):
                    check = vert[c]                                                 # Vai iterando e vendo o vertice
                    K = list(G.neighbors(check))
                    op_exaustive = op_exaustive + 1                                 # Para contar o número de operações -> dentro do for mais interior
                    if check not in S:                                              # Definição de set dominante -> Todo o vertice não em S
                        if any(i in K for i in S):                                  # É adjacente a pelo menos 1 vertice em S
                            result[c] = 1
                        else:
                            result[c] = -1                                          # Para invalidar os sets

                if -1 not in result:                                                # Se o set é válido pode retornar e parar a execução
                    return S
            testing += 1                                                            # Caso não seja uma que se pretende analisar, incrementa-se para passar para a próxima combinação

        return []

def main():
    #global op_exaustive                                                     # Contador do número de operação básicas para o Algortimo Exaustivo
    
    global Total_Tested                                                      # Contador do número de tamanhos testados (não era preciso ser global)


    P_list = [0.125,0.25,0.5,0.75]                                           # Dado duas arestas P corresponde a probabilidade de ela existir, serve para tornar os grafos mais/menos densos
    #S = [x for x in range(4,10)]                                            # Tamanho do grafo
    S = [25]

    for z in range(len(P_list)):
        P = P_list[z]
        print("\nP =",P)

        e_time = [0 for x in range(len(S))]                                 # Tempo 
        e_op = [0 for x in range(len(S))]                                   # Operações 
        #n_solutions_E = [0 for x in range(len(S))]                         # Nº Soluções
        n_config_E = [0 for x in range(len(S))]                             # Nº Configurações
        k_vector = [0 for x in range(len(S))]
        solutions = [0 for x in range(len(S))]

        for w in range(len(S)):
            s = S[w]
            print("\nN vertice:",s)

            op_best = 10**50                                                # Valor muito elevado, impossivel, para depois se poder atualizar

        
            G = generate_graph(s,P)
            print("Dominating set:")
            print(nX.dominating_set(G))
                         
            #coord = coordinates(s)                                         # Gerar coordenadas dos vértices

            tamanhos = [x for x in range(1,s+1)]
            Total_Tested = 1

            test_max = min(s-1,10)

            while(Total_Tested <= test_max):

                ta = random.randint(0,len(tamanhos)-1)                      # Escolhe um indice de um tamanho

                K = tamanhos[ta]                                            # Tamanho com indice ta

                tamanhos.pop(ta)                                            # Elima o tamanho que vai ser analisado

                print("\nK = ", K, "( Tentativa :", Total_Tested,")")
                print("Comprimento do dominating set tem que ser:", K)

                tic = time.perf_counter()

                S_E = exaustive(s,K,G)
                toc = time.perf_counter()
                if len(S_E) != 0:                                           # Caso encontre solução

                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))        # Verificar se é Dominating Set

                    if op_exaustive < op_best:                              # compara o nº de operações com a melhor até ao momento
                        op_best = op_exaustive                              # atualiza o melhor número (menor valor) de operações

                        e_time[w] = toc-tic
                        e_op[w] = op_best
                        n_config_E[w] = N_conf_E
                        k_vector[w] = K
                        solutions[w] = set(S_E)
                        
                else:
                    print("No result") 
                            

                print(f"Time: {toc - tic:0.4f} seconds")

                Total_Tested += 1
        
        print("Size:", S)
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
            f.write("\n"+"N_Configurations ="+ str(n_config_E)+";")
            f.write("\n"+"Solutions ="+ str(solutions)+";")
            f.write("\n")

            #f.close()
    



if __name__ == "__main__":
   main()


