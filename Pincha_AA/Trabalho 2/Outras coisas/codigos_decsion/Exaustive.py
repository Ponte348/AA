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

# Cria o ficheiro txt para os resultados e formata o header
def make_txt_header():
    with open("C:/Users/OMEN/Desktop/Output_98012.txt","w") as f:
        f.write("_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%")
        f.write("\nExplicação do cabeção")
        f.write("\nKs_analyzed -> Tamanhos analisados")
        f.write("\nOperacoes -> Número de operações")
        f.write("\nTempos_tentados -> Tempo de execução")
        f.write("\nN_Configurations -> Número de combinações analisadas")
        f.write("\nSolutions -> Conjunto Domiante encontrado (if 0 -> no set found)")
        f.write("\nCheck_if_correct -> Verificar se é realmente um conjunto dominante, 1(V) 0(F) -1(se não foi encontrada solução)")
        f.write("\n_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%\n")


# Algoritmo Exaustivo
def exaustive(s,k,G):
    global op_exaustive
    global N_conf_E
    N_conf_E = 0                                                            # Variavel para contar o nº de Configurações
    op_exaustive = 0                                                        # Variavel para contar o nº de operações

    vert = [x for x in range(s)]                                            # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]

    Length = k

    list_combinations = []                                                  # Vamos ver todas as combinações possíveis
    for n in range(len(vert) + 1):                                          # Pondo tudo dentro deste for torna-se mais rapidos pois não se guarda todas as combinações possiveis, o que para grafos grandes tornava-se bastante dispendioso
        for comb in combinations(vert, n):
            if len(comb) == Length:                                         # Apenas queremos as combinações com o tamanho pretendido
                list_combinations.append(comb)

        n_comb = len(list_combinations)

        for a in range(n_comb):
            N_conf_E = N_conf_E + 1
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

    graf_in = 4
    graf_fin = 30

    P_list = [0.125,0.25,0.5,0.75]                                           # Dado duas arestas P corresponde a probabilidade de ela existir, serve para tornar os grafos mais/menos densos
    S = [x for x in range(graf_in,graf_fin+1)]                                             # Tamanho do grafo

    make_txt_header()


    for z in range(len(P_list)):
        P = P_list[z]
        print("\nP =",P)


        # Para Guardar todos os parâmetros
        e_op = []                                                           # Operações para cada (P,S)
        n_config_E = []                                                     # Nº Configurações para cada (P,S)
        times = []                                                          # Vetor com os tempos que demorou cada (P,S)
        solutions = []                                                      # Solução encontrada para cada par (P,S)
        ks_analyzed = []                                                    # Ks analisados para cada par (P,S)
        check_if_correct = []                                               # Confirmar que o conjunto dominante encontrado está correto, 1-Correto 0-Incorreto, -1 se não foi encontrado nenhum resultado

        for w in range(len(S)):
            s = S[w]

            K = [x for x in range(1, s)]

            # Gerar gráfico
            G = generate_graph(s,P)

            # Para Guardar todos os parâmetros
            operacoes = []                                                         # Operações para cada (S,K)
            configuracoes = []                                                     # Nº Configurações para cada (S,K)
            tempos = []                                                            # Vetor com os tempos que demorou cada (S,K)
            solucoes = [0 for x in range(1,s)]                                     # Solução encontrada para cada par (S,K) - 0 se não foi encontrada solução, 1 - se foi
            is_correct = [-1 for x in range(1,s)]                                  # Confirmar que o conjunto dominante encontrado está correto, 1-Correto 0-Incorreto, -1 se não foi encontrado nenhum resultado

            for r in range(len(K)):
                k = K[r]

                print("\nK = ", k,", for Size =",s," and P =",P)

                tic = time.perf_counter()

                S_E = exaustive(s,k,G)
                toc = time.perf_counter()

                if len(S_E) != 0:
                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))        # Verificar se é Dominating Set
                    solucoes[r] = set(S_E)

                    if nX.is_dominating_set(G, set(S_E)) == True:
                        is_correct[r] = 1
                    else:
                        is_correct[r] = 0

                else:
                    print("\nNo result found")

                TIME_TAKEN = toc - tic
                print(f"Time: {TIME_TAKEN:0.4f} seconds")

                operacoes.append(op_exaustive)
                configuracoes.append(N_conf_E)
                tempos.append(TIME_TAKEN)
                

            e_op.append(operacoes)
            n_config_E.append(configuracoes)
            times.append(tempos)
            solutions.append(solucoes)
            check_if_correct.append(is_correct)
            ks_analyzed.append(K)

        with open("C:/Users/OMEN/Desktop/Output_98012.txt","a") as f:
            f.write("\n\n%Todos os parâmetros")
            f.write("\n"+"P ="+str(P)+";"+"\nSize ="+str(S)+";")
            f.write("\n"+"Ks_analyzed ="+ str(ks_analyzed)+";")
            f.write("\n"+"Operacoes ="+ str(e_op)+";")
            f.write("\n"+"Tempos_tentados ="+ str(times)+";")
            f.write("\n"+"N_Configurations ="+ str(n_config_E)+";")
            f.write("\n"+"Solutions ="+ str(solutions)+";")
            f.write("\n"+"Is_Correct ="+ str(check_if_correct)+";")
    



if __name__ == "__main__":
   main()


