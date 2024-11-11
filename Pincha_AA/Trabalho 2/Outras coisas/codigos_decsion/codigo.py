## Importar as packages necessárias

import networkx as nX
import matplotlib.pyplot as plt
import math
import random
from itertools import combinations
import time
#import numpy as np

random.seed(98012)

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
        f.write("\nKs_analyzed -> Tamanhos analisados")
        f.write("\nOperacoes -> Número de operações")
        f.write("\nTempos_tentados -> Tempo de execução")
        f.write("\nN_Configurations -> Número de combinações analisadas")
        f.write("\nSolutions -> Conjunto Domiante encontrado (if 0 -> no set found)")
        f.write("\nCheck_if_correct -> Verificar se é realmente um conjunto dominante, 1(V) 0(F) -1(se não foi encontrada solução)")
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
        List.append(D)
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

    if type(usr_confs) is float:
        conf_max = math.ceil(n_comb*usr_confs)
    else:
        conf_max = min(n_comb,usr_confs)

    print("\nGonna Analyze at max",int(conf_max),"combinations")

    while (N_conf_E<=int(conf_max)):        
        print("Now in Configuração:",N_conf_E)

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

        if (N_conf_E == int(conf_max)):                                     # Foi preciso adicionar este if pois estava a dar em erro no while (no fim dava +1 combinação analisada do que realemente foi)
            break
        else:
            N_conf_E = N_conf_E + 1                                         # Incrementa o número de configurações analisadas

    return []


def main():

    usr_confs = 100                                                           # Número máximo de configurações para serem analisadas. Caso este número seja maior que o número de configurações possiveis, o número máximo de configurações analisadas será então o número de combinações possiveis

    graf_in = 4
    graf_fin = 51

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

                S_E = check_dominating_set(s,k,usr_confs,G)
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


''''
            e_time = [0 for x in range(len(S))]                             # Tempo Exaustiva
            e_op = [0 for x in range(len(S))]                               # Operações Exaustiva 
            n_solutions_E = [0 for x in range(len(S))]                      # Nº Soluções Exaustiva
            n_config_E = [0 for x in range(len(S))]                         # Nº Configurações Exaustiva

            for r in range(len(K)):
                k = K[r]

        with open("C:/Users/OMEN/Desktop/Output_98012.txt","a") as f:
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
'''

if __name__ == "__main__":
   main()
