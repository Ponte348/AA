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
        coord[i][0] = random.randint(0,21)
        coord[i][1] = random.randint(0,21)


    return coord

def make_txt_header():
    with open("C:/Users/OMEN/Desktop/Output_98012.txt","a") as f:
        f.write("_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%")
        f.write("\nExplicação do cabeção")
        f.write("\nKs -> Tamanho de conjunto dominante com menos operaçõe efetuadass")
        f.write("\nOperacoes -> Optimal number of operações")
        f.write("\nTempo -> Tempo para encontrar o conjunto dominante com menos operações efetuadas")
        f.write("\nSolutions -> Conjunto dominante com menos operações efetuadas")
        f.write("\n_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%\n")


# Algoritmo1
def exaustive(s,K,usr_confs,G):
    global op_exaustive
    global N_conf_E
    
    N_conf_E = 1                                                            # Variavel para contar o nº de Configurações
    op_exaustive = 0                                                        # Variavel para contar o nº de operações

    vert = [x for x in range(s)]                                            # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]

    Length = K

    list_combinations = []                                                  # Vamos ver todas as combinações possíveis
    for n in range(len(vert) + 1):                                          # Pondo tudo dentro deste for torna-se mais rapidos pois não se guarda todas as combinações possiveis, o que para grafos grandes tornava-se bastante dispendioso
        for comb in combinations(vert, n):
            if len(comb) == Length:                                         # Apenas queremos as combinações com o tamanho pretendido
                list_combinations.append(comb)
    
    n_comb = len(list_combinations)
    conf_max = min(n_comb-1,usr_confs)
    
    print("\nGonna Analyze",conf_max,"combinations")

    while (N_conf_E<=conf_max):
        print("Now in combination:",N_conf_E)

        idx = random.randint(0,len(list_combinations)-1)                    # Escolhe um indice de uma configuração

        S = list(list_combinations[idx])                                    # Vai iterando e vendo a combinação

        list_combinations.pop(idx)                                          # Elima a configuração que vai ser analisada

        result =  [0 for x in range(s)]
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

        N_conf_E = N_conf_E + 1                                             # Incrementa o número de configurações analisadas

    return []                                                               # Se chegar ao fim e não encontrar retorna o conjunto vazio

# Algoritmo 2
def exaustive_v2(Size,n,usr_perc,G):
        global op_exaustive
        global N_conf_E
    
        N_conf_E = 1                                                            # Variavel para contar o nº de Configurações

        op_exaustive = 0                                                        # Variavel para contar o nº de operações
        
        number_of_combinations = math.factorial(Size)/(math.factorial(n)*math.factorial(Size-n))        # Número total possivel de combinações de tamanho n com Size vertices

        k = math.ceil(number_of_combinations*usr_perc)                              # Apenas queremos x % dessas combinações para análise

        print("\nGonna Analyze",k,"combinations")

        to_test = list(random.sample(range(int(number_of_combinations)),k))     # Gera k números random correspondestes ao número da combinações para analise, p.ex. 1-> combinação nº1
        

        testing = 0

        vert = [x for x in range(Size)]

        for S in combinations(vert, n):                                             # Itera em todas as combinações
            if testing in to_test:                                                  # Caso seja uma que se pretende analisar
                #print("Now in combination:", N_conf_E)
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
    global Total_Tested                                                      # Contador do número de tamanhos testados (não era preciso ser global)

    usr_confs = 10                                                           # Número máximo de configurações para serem analisadas. Caso este número seja maior que o número de configurações possiveis, o número máximo de configurações analisadas será então o número de combinações possiveis
    usr_perc = 0.10                                                          # % do número de combinações que se quer analisar

    P_list = [0.125,0.25,0.5,0.75]                                          # Dado duas arestas P corresponde a probabilidade de ela existir, serve para tornar os grafos mais/menos densos
    #S = [x for x in range(15,20)]                                           # Tamanho do grafo
    S = [30]
    make_txt_header()                                                       # Faz o header do ficheiro txt com os resultados


    for z in range(len(P_list)):
        P = P_list[z]
        print("\nP =",P)

        e_time = [0 for x in range(len(S))]                                 # Tempo 
        e_op = [0 for x in range(len(S))]                                   # Operações 
        n_config_E = [0 for x in range(len(S))]                             # Nº Configurações
        k_vector = [0 for x in range(len(S))]                               # Melhor tamanhos
        solutions = [0 for x in range(len(S))]                              # Melhores soluções

        e_time_v2 = [0 for x in range(len(S))]                              # Tempo 
        e_op_v2 = [0 for x in range(len(S))]                                # Operações 
        n_config_E_v2 = [0 for x in range(len(S))]                          # Nº Configurações
        k_vector_v2 = [0 for x in range(len(S))]                            # Melhor tamanhos
        solutions_v2 = [0 for x in range(len(S))]                           # Melhores soluções


        for w in range(len(S)):
            s = S[w]
            print("\nN vertice:",s)

            op_best = 10**50                                                # Algoritmo 1 - Valor muito elevado, impossivel, para depois se poder atualizar
            op_best2 = 10**50                                               # Algoritmo 2 - Valor muito elevado, impossivel, para depois se poder atualizar
        
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

                print("\nK = ", K, "( Tentativa :", Total_Tested,") for Size =",s," and P =",P)
                print("Comprimento do dominating set tem que ser:", K)

                tic = time.perf_counter()

                S_E = exaustive(s,K,usr_confs,G)
                toc = time.perf_counter()
                if len(S_E) != 0:                                           # caso encontre solução

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

                print(f"Time Algoritmo 1: {toc - tic:0.4f} seconds")

                tic = time.perf_counter()

                S_E_v2 = exaustive_v2(s,K,usr_perc,G)
                toc = time.perf_counter()
                if len(S_E_v2) != 0:                                           # caso encontre solução

                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E_v2)))        # Verificar se é Dominating Set

                    if op_exaustive < op_best2:                              # compara o nº de operações com a melhor até ao momento
                        op_best2 = op_exaustive                              # atualiza o melhor número (menor valor) de operações

                        e_time_v2[w] = toc-tic
                        e_op_v2[w] = op_best2
                        n_config_E_v2[w] = N_conf_E
                        k_vector_v2[w] = K
                        solutions_v2[w] = set(S_E_v2)
                        
                else:
                    print("No result")  
                            

                print(f"Time Algoritmo 2: {toc - tic:0.4f} seconds")

                Total_Tested += 1
        
        #print("Size:", S)
        #print("Best Operações:", e_op)
        #print("Times:", e_time)
        #print("Configurações: ", n_config_E)
        #print("Ks:", k_vector)
        #print("Solutions:", solutions)


        with open("C:/Users/OMEN/Desktop/Output_98012.txt","a") as f:
            f.write("\nSize ="+str(S)+"; P ="+str(P)+";")
            f.write("\n\nFunção 1")
            f.write("\n"+"Ks ="+ str(k_vector)+";")
            f.write("\n"+"Operacoes ="+ str(e_op)+";")
            f.write("\n"+"Tempo ="+ str(e_time)+";")
            f.write("\n"+"N_Configurations ="+ str(n_config_E)+";")
            f.write("\n"+"Solutions ="+ str(solutions)+";")

            f.write("\n\nFunção 2")
            f.write("\n"+"Ks ="+ str(k_vector_v2)+";")
            f.write("\n"+"Operacoes ="+ str(e_op_v2)+";")
            f.write("\n"+"Tempo ="+ str(e_time_v2)+";")
            f.write("\n"+"N_Configurations ="+ str(n_config_E_v2)+";")
            f.write("\n"+"Solutions ="+ str(solutions_v2)+";")
            f.write("\n")

            #f.close()
    



if __name__ == "__main__":
   main()


