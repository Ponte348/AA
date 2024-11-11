## Importar as packages necessárias

import networkx as nX
import matplotlib.pyplot as plt
from math import floor
import random
from itertools import combinations
import time
#import numpy as np

# Fixar a seed
random.seed(98012)

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
    with open("C:/Users/OMEN/Desktop/Heuristic.txt","w") as f:
        f.write("_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%")
        f.write("\nExplicação do cabeçalho")
        f.write("\nKs -> Tamanho de conjuntos dominantes analisados correspondente ao valor de Size(i)")
        f.write("\nOperacoes -> Número de operações correspondente ao par (K, Size)")
        f.write("\nTempo -> Tempo de execução correspondente ao par (K, Size) ")
        f.write("\nSolutions -> Conjunto dominante minimo")
        f.write("\nCheck_if_correct -> Verificar se é realmente um conjunto dominante, 1(V) 0(F) -1(se não foi encontrado nenhum set)")
        f.write("\nNota: Na divisão -> Parâmetros correspondentes ao K que retornou solução <- caso exista o valor 0 nas variaveis Ks_solutions, Operacoes, Tempo, N_configurations, Solutions quer dizer que não foi encontra nenhuma solução (0 é o valor default)")
        f.write("\n_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%\n")


# Algortimo Heuristico
def heuristc(s,k,G,Vert_Init):
    global op_heuristic    
    global N_conf_H
    N_conf_H = 0                                                            # Variavel para contar o nº de Configurações
    op_heuristic = 0                                                        # Variavel para contar o nº de operações

    vert = [x for x in range(s)]                                            # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]
    

    Length = k                                                              # Tamanho do set que se quer

    list_combinations = []                                                  # Vamos ver todas as combinações possíveis
    for n in range(len(vert) + 1):                                          # Pondo tudo dentro deste for torna-se mais rapidos pois não se guarda todas as combinações possiveis, o que para grafos grandes tornava-se bastante dispendioso
        for comb in combinations(vert, n):
            if Vert_Init in comb:                                           # Opção Heuristica - Apenas ver sets que contenham o vértice Vert_Init, na solução proposta este valor é 0 
                if len(comb) == Length:                                     # Apenas queremos as combinações com o tamanho pretendido
                    list_combinations.append(comb)


        n_comb = len(list_combinations)

        for a in range(n_comb):
            N_conf_H = N_conf_H + 1
            S = list(list_combinations[a])                                  # Vai iterando e vendo a combinação
            result =  [0 for x in range(s)]
            for c in range(len(vert)):
                op_heuristic = op_heuristic + 1                             # Para contar o número de operações -> dentro do for mais interior
                check = vert[c]                                             # Vai iterando e vendo o vertice
                K = list(G.neighbors(check))
                if check not in S:                                          # Definição de set dominante -> Todo o vertice não em S
                    if any(i in K for i in S):                              # É adjacente a pelo menos 1 vertice em S
                        result[c] = 1
                    else:
                        result[c] = -1                                      # Para invalidar os sets

            if -1 not in result:                                            # Se o set é válido pode retornar e parar a execução
                return S


    return []                                                               # Se chegar ao fim e não encontrar retorna o conjunto vazio



def main():

    start = time.time()

    P_list = [0.125,0.25,0.5,0.75]                                          # Dado duas arestas P corresponde a probabilidade de ela existir, serve para tornar os grafos mais/menos densos
    
    tamanho_ininical = 4
    tamanho_final = 30
    
    S = [x for x in range(tamanho_ininical,tamanho_final + 1)]              # Tamanho do grafo

    make_txt_header()

    Vert_Init = 0


    for z in range(len(P_list)):
        P = P_list[z]
        print("\nP =",P)

        # Caso haja solução, guarda os valores de cada solução
        SOL_e_time = [0 for x in range(len(S))]                              # Tempo 
        SOL_e_op = [0 for x in range(len(S))]                                # Operações 
        SOL_n_config_E = [0 for x in range(len(S))]                          # Nº Configurações
        SOL_k_vector = [0 for x in range(len(S))]                            # Tamanho que deu uma solução
        SOL_solutions = [0 for x in range(len(S))]                           # Conjunto que é solução
        SOL_is_correct = [-1 for x in range(len(S))]                         # Confirmar que o conjunto dominante encontrado está correto, 1-Correto 0-Incorreto

        # Para guardar os parâmetros que serão usados para fazer os gráficos
        TOTAL_OPS = []                                                       # Soma de todas as operações
        TOTAL_TIME = []                                                      # Soma de todos os tempos
        TOTAL_CONFS = []                                                     # Soma de todas as configurações analisadas

        # Para Guardar todos os parâmetros
        e_op = []                                                            # Operações para cada S
        n_config_E = []                                                      # Nº Configurações para cada S
        k_vector = []                                                        # Tamanhos testados para cada S
        Time_trys = []                                                       # Vetor com os tempos que demorou cada S

        for w in range(len(S)):
            s = S[w]

            print("\nN vertice:",s)
        
            G = generate_graph(s,P)
            print(nX.dominating_set(G))
                
            #coord = coordinates(s)                                          # Gerar coordenadas dos vértices

            tamanhos = [x for x in range(1,s)]

            m = 0
            Result = -2

            op_tentados = []
            confs_tentados = []
            k_tentados = []
            times_tentados = []

            total_ops = 0
            total_confs = 0
            total_time = 0

            while(Result != -1):

                if m == s-1:
                    break

                K = tamanhos[m]                                              # Tamanho com indice m

                m += 1


                print("\nK = ", K, "( Tentativa :", K,") for Size =",s," and P =",P)

                tic = time.perf_counter()

                S_E = heuristc(s,K,G,Vert_Init)
                toc = time.perf_counter()
                total_ops = total_ops + op_heuristic
                total_confs = total_confs + N_conf_H
                total_time = total_time + (toc-tic)

                if len(S_E) != 0:                                             # caso encontre solução

                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))        # Verificar se é Dominating Set

                    if nX.is_dominating_set(G, set(S_E)) == True:
                        SOL_is_correct[w] = 1
                    else:
                        SOL_is_correct[w] = 0

                    SOL_e_time[w] = toc-tic
                    SOL_e_op[w] = op_heuristic
                    SOL_n_config_E[w] = N_conf_H
                    SOL_k_vector[w] = K
                    SOL_solutions[w] = set(S_E)

                    Result = -1                                                 # Encontrou uma solução pode parar
                        
                else:
                    print("No result")
                            

                print(f"Time: {toc - tic:0.4f} seconds")
                tempo_do_k = toc - tic
                
                # Guardar todos os parametros
                times_tentados.append(tempo_do_k)
                op_tentados.append(op_heuristic)
                confs_tentados.append(N_conf_H)
                k_tentados.append(K)

            # Guardar no array final
            Time_trys.append(times_tentados)
            e_op.append(op_tentados)
            n_config_E.append(confs_tentados)
            k_vector.append(k_tentados)

            # Guardar soma dos parâmetros, para os gráficos
            TOTAL_OPS.append(total_ops)
            TOTAL_CONFS.append(total_confs)
            TOTAL_TIME.append(total_time)

        print("End P =",P,"\n")

        with open("C:/Users/OMEN/Desktop/Heuristic.txt","a") as f:
            f.write("\n\n%Todos os parâmetros")
            f.write("\n"+"P ="+str(P)+";"+"\nSize ="+str(S)+";")
            f.write("\n"+"Ks ="+ str(k_vector)+";")
            f.write("\n"+"Operacoes ="+ str(e_op)+";")
            f.write("\n"+"Tempos_tentados ="+ str(Time_trys)+";")
            f.write("\n"+"N_Configurations ="+ str(n_config_E)+";")

            f.write("\n\n%Parâmetros correspondentes ao K que retornou solução")
            f.write("\n"+"Ks_solution ="+ str(SOL_k_vector)+";")
            f.write("\n"+"Operacoes ="+ str(SOL_e_op)+";")
            f.write("\n"+"Tempo ="+ str(SOL_e_time)+";")
            f.write("\n"+"N_Configurations ="+ str(SOL_n_config_E)+";")
            f.write("\n"+"Solutions ="+ str(SOL_solutions)+";")
            f.write("\n"+"Check_if_correct ="+ str(SOL_is_correct)+";")

            f.write("\n\n%Parâmetros para gráficos")
            f.write("\n"+"Total_operacoes ="+ str(TOTAL_OPS)+";")
            f.write("\n"+"Total_configurations ="+ str(TOTAL_CONFS)+";")
            f.write("\n"+"Total_time ="+ str(TOTAL_TIME)+";")
            f.write("\n")

            #f.close()
    end = time.time()

    print('Total Time:', end - start,'(s)')   



if __name__ == "__main__":
   main()


