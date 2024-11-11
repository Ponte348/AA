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

# Cria o ficheiro txt para os resultados e formata o header
def make_txt_header():
    with open("C:/Users/OMEN/Desktop/Output_98012.txt","w") as f:
        f.write("_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%")
        f.write("\nExplicação do cabeção")
        f.write("\nKs -> Tamanho de conjunto dominante com menos operaçõe efetuadass")
        f.write("\nOperacoes -> Optimal number of operações")
        f.write("\nTempo -> Tempo para encontrar o conjunto dominante com menos operações efetuadas")
        f.write("\nSolutions -> Conjunto dominante com menos operações efetuadas")
        f.write("\nCheck_if_correct -> Verificar se é realmente um conjunto dominante, 1(V) 0(F) -1(se não foi encontrada solução)")
        f.write("\nNota: Na divisão -> Parâmetros correspondentes ao K que retornou solução <- caso exista o valor 0 nas variaveis Ks_solutions, Operacoes, Tempo, N_configurations, Solutions quer dizer que não foi encontra nenhuma solução (0 é o valor default) ")
        f.write("\n_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%\n")



# Algoritmo
def combinations_generator(s,k):
    global List
    global op_exaustive
    
    vect = [x for x in range(s)]
    count = 0

    D = []
    while(count != k):
        idx = random.randint(0,len(vect)-1) 
        v = vect[idx]
        D.append(v)
        vect.pop(idx)
        count += 1
        op_exaustive +=1

    if D not in List and len(D) == k:
        return D
    else:
        combinations_generator(s,k)

def check_dominating_set(Size,n,usr_confs,G):
    global List
    global N_conf_E
    global op_exaustive

    op_exaustive = 0

    N_conf_E = 1

    List = []

    vert = [x for x in range(Size)]


    n_comb = math.factorial(Size)/(math.factorial(n)*math.factorial(Size-n))
    #print(n_comb)

    if type(usr_confs) is float:
        conf_max = math.ceil(n_comb*usr_confs)
        #print(conf_max)
    else:
        conf_max = min(n_comb,usr_confs)

    print("\nGonna Analyze at max",int(conf_max),"combinations")

    while (N_conf_E<=int(conf_max)):        
        #print("Now in Configuração:",N_conf_E)

        S = combinations_generator(Size,n)

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

        N_conf_E = N_conf_E + 1                                             # Incrementa o número de configurações analisadas

    return []


def main():

    usr_confs = 1000000                                                           # Número máximo de configurações para serem analisadas. Caso este número seja maior que o número de configurações possiveis, o número máximo de configurações analisadas será então o número de combinações possiveis


    P_list = [0.125,0.25,0.5,0.75]                                           # Dado duas arestas P corresponde a probabilidade de ela existir, serve para tornar os grafos mais/menos densos
    S = [x for x in range(4,6)]                                             # Tamanho do grafo

    make_txt_header()


    for z in range(len(P_list)):
        P = P_list[z]
        print("\nP =",P)

        # Caso haja solução, guarda os valores de cada solução
        SOL_e_time = [0 for x in range(len(S))]                                 # Tempo 
        SOL_e_op = [0 for x in range(len(S))]                                   # Operações 
        SOL_n_config_E = [0 for x in range(len(S))]                             # Nº Configurações
        SOL_k_vector = [0 for x in range(len(S))]                               # Tamanho que deu uma solução
        SOL_solutions = [0 for x in range(len(S))]                              # Conjunto que é solução
        SOL_is_correct = [-1 for x in range(len(S))]                            # Confirmar que o conjunto dominante encontrado está correto, 1-Correto 0-Incorreto

        # Para Guardar todos os parâmetros
        e_op = []                                                           # Operações para cada S
        n_config_E = []                                                     # Nº Configurações para cada S
        k_vector = []                                                       # Tamanhos testados para cada S
        Time_trys = []                                                      # Vetor com os tempos que demorou cada S

        for w in range(len(S)):
            s = S[w]

            print("\nN vertice:",s)
        
            G = generate_graph(s,P)
            print(nX.dominating_set(G))
                
            #coord = coordinates(s)                                         # Gerar coordenadas dos vértices

            tamanhos = [x for x in range(1,s)]

            m = 0
            Result = -2

            op_tentados = []
            confs_tentados = []
            k_tentados = []
            times_tentados = []

            while(Result != -1):

                if m == s-1:
                    break

                K = tamanhos[m]                                            # Tamanho com indice m

                m += 1


                print("\nK = ", K, "( Tentativa :", K,") for Size =",s," and P =",P)

                tic = time.perf_counter()

                S_E = check_dominating_set(s,K,usr_confs,G)
                toc = time.perf_counter()
                if len(S_E) != 0:                                           # caso encontre solução

                    print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))        # Verificar se é Dominating Set

                    if nX.is_dominating_set(G, set(S_E)) == True:
                        SOL_is_correct[w] = 1
                    else:
                        SOL_is_correct[w] = 0

                    SOL_e_time[w] = toc-tic
                    SOL_e_op[w] = op_exaustive
                    SOL_n_config_E[w] = N_conf_E
                    SOL_k_vector[w] = K
                    SOL_solutions[w] = set(S_E)

                    Result = -1                                 # Encontrou uma solução pode parar
                        
                else:
                    print("No result")
                            

                print(f"Time: {toc - tic:0.4f} seconds")
                tempo_do_k = toc - tic
                
                # Guardar todos os parametros
                times_tentados.append(tempo_do_k)
                op_tentados.append(op_exaustive)
                confs_tentados.append(N_conf_E)
                k_tentados.append(K)

            # Guardar no array final
            Time_trys.append(times_tentados)
            e_op.append(op_tentados)
            n_config_E.append(confs_tentados)
            k_vector.append(k_tentados)

        
        print("Size:", S)
        print("Best Operações:", SOL_e_op)
        print("Times:", SOL_e_time)
        print("Configurações: ", SOL_n_config_E)
        print("Ks with solution:", SOL_k_vector)
        print("Solutions:", SOL_solutions)
        print("Is correct:",SOL_is_correct)


        with open("C:/Users/OMEN/Desktop/Output_98012.txt","a") as f:
            f.write("\n\n%Todos os parâmetros")
            f.write("\n"+"Size ="+str(S)+"; P ="+str(P)+";")
            f.write("\n"+"Ks_solution ="+ str(k_vector)+";")
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
            f.write("\n")

            #f.close()


if __name__ == "__main__":
   main()
