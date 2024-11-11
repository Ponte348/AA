## Importar as packages necessárias

import networkx as nX
import matplotlib.pyplot as plt
import math
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
        coord[i][0] = random.randint(0,21)
        coord[i][1] = random.randint(0,21)


    return coord

# Cria o ficheiro txt para os resultados e formata o header
def make_txt_header(usr_confs):
    with open("C:/Users/OMEN/Desktop/Randomized.txt","w") as f:
        f.write("_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%")
        f.write("\nExplicação do cabeçalho")
        f.write("\nKs -> Tamanho de conjuntos dominantes analisados correspondente ao valor de Size(i)")
        f.write("\nOperacoes -> Número de operações correspondente ao par (K, Size)")
        f.write("\nTempo -> Tempo de execução correspondente ao par (K, Size) ")
        f.write("\nSolutions -> Conjunto dominante minimo")
        f.write("\nCheck_if_correct -> Verificar se é realmente um conjunto dominante, 1(V) 0(F) -1(se não foi encontrado nenhum set)")
        f.write("\nNota: Na divisão -> Parâmetros correspondentes ao K que retornou solução <- caso exista o valor 0 nas variaveis Ks_solutions, Operacoes, Tempo, N_configurations, Solutions quer dizer que não foi encontra nenhuma solução (0 é o valor default)")
        f.write("\n"+"Nº de configurações analisadas para cada valor de K = min(N_combinações, "+ str(usr_confs)+");")
        f.write("\n_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%\n")



# Cria um conjunto de S com tamanho K, verifica se o conjunto criado já foi analisado
def combinations_generator(s,k):
    global List
    global op_exaustive
    
    vect = [x for x in range(s)]
    count = 0

    D = []
    while(len(D) != k):
        idx = random.randint(0,len(vect)-1) 
        v = vect[idx]
        D.append(v)
        vect.pop(idx)
        count = count + 1
        op_exaustive = op_exaustive + 1

    if D not in List:
        List.append(D)
        return D
    else:
        D = combinations_generator(s,k)

    return D

# Algoritmo que verifica se é conjunto dominante
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

        S = combinations_generator(Size,n)

        result =  [0 for x in range(Size)]
        for c in range(len(vert)):
            check = vert[c]                                                         # Vai iterando e vendo o vertice
            K = list(G.neighbors(check))
            op_exaustive = op_exaustive + 1                                         # Para contar o número de operações -> dentro do for mais interior
            if check not in S:                                                      # Definição de set dominante -> Todo o vertice não em S
                if any(i in K for i in S):                                          # É adjacente a pelo menos 1 vertice em S
                    result[c] = 1
                else:
                    result[c] = -1                                                  # Para invalidar os sets

        if -1 not in result:                                                        # Se o set é válido pode retornar e parar a execução
            return S

        if (N_conf_E == int(conf_max)):                                             # Foi preciso adicionar este if pois estava a dar em erro no while (no fim dava +1 combinação analisada do que realemente foi)
            break
        else:
            N_conf_E = N_conf_E + 1                                                 # Incrementa o número de configurações analisadas

    return []


def create_graph(path, D):
    # O ficheiro tem que estar no formato:
    # 0 / 1 É grafo orientado ?
    # 0 / 1 Há pesos associados às arestas ?
    # Número de vértices
    # Número de arestas
    # Vértice inicial vértice final (peso, se existir)

    count = 1
    with open(path) as f:
        w = [int(x) for x in next(f).split()] # lê a primeira linha
        array = []
        for line in f: # lê as restantes linhas
            if count > 3:
                array.append([x for x in line.split()])
            if count == 2:
                size = [int(x) for x in line.split()]

            count += 1
    
    if D == 1:
        G = nX.DiGraph()                                                        # Grafo Direcionado
    else:
        G = nX.Graph()                                                          # Grafo não direcionado

    for i in range(len(array)):
        e1 = int(array[i][0])
        e2 = int(array[i][1])
        G.add_edge(e1, e2)

    size = size[0]

    return G, size


def main():

    usr_confs = 1000                                                            # Número máximo de configurações para serem analisadas. Caso este número seja maior que o número de configurações possiveis, o número máximo de configurações analisadas será então o número de combinações possiveis

    make_txt_header(usr_confs)


    # Caso haja solução, guarda os valores de cada solução
    SOL_e_time = []                                                             # Tempo 
    SOL_e_op = []                                                               # Operações 
    SOL_n_config_E = []                                                         # Nº Configurações
    SOL_k_vector = []                                                           # Tamanho que deu uma solução
    SOL_solutions = []                                                          # Conjunto que é solução
    SOL_is_correct = []                                                         # Confirmar que o conjunto dominante encontrado está correto, 1-Correto 0-Incorreto

    # Para guardar os parâmetros que serão usados para fazer os gráficos
    TOTAL_OPS = []                                                              # Soma de todas as operações
    TOTAL_TIME = []                                                             # Soma de todos os tempos
    TOTAL_CONFS = []                                                            # Soma de todas as configurações analisadas


    path = 'C:/Users/OMEN/Desktop/SWmediumDG.txt'                               # Caminho para o ficheiro txt que contem o grafo
    is_directed = 1                                                             # 1 - Direcionado, 0 - Não Direcionado

    G, s = create_graph(path, is_directed)
       
    print("\nN vertice:",s) 
    #coord = coordinates(s)                                                     # Gerar coordenadas dos vértices

    start = time.time()

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

        K = tamanhos[m]                                                     # Tamanho da lista 'tamanhos' com indice m

        m += 1


        print("\nK = ", K, "( Tentativa :", m,") for Size =",s)

        tic = time.perf_counter()

        S_E = check_dominating_set(s,K,usr_confs,G)
        toc = time.perf_counter()
        total_ops = total_ops + op_exaustive
        total_confs = total_confs + N_conf_E
        total_time = total_time + (toc-tic)

        if len(S_E) != 0:                                                   # caso encontre solução

            print("\nExaustiva Set is Dominating?-> ",nX.is_dominating_set(G, set(S_E)))        # Verificar se o que foi retornado é realmente Dominating Set

            if nX.is_dominating_set(G, set(S_E)) == True:
                
                SOL_is_correct.append(1)
                SOL_e_time.append(toc-tic)
                SOL_e_op.append(op_exaustive)
                SOL_n_config_E.append(N_conf_E)
                SOL_k_vector.append(K)
                SOL_solutions.append(set(S_E))

                Result = -1                                                 # Encontrou uma solução pode parar
            else:
                SOL_is_correct.append(0)
                
        else:
            print("No result")
                    

        print(f"Time: {toc - tic:0.4f} seconds")
        tempo_do_k = toc - tic
        
        # Guardar todos os parametros
        times_tentados.append(tempo_do_k)
        op_tentados.append(op_exaustive)
        confs_tentados.append(N_conf_E)
        k_tentados.append(K)

        if Result == -1:
            break


    # Guardar soma dos parâmetros, para os gráficos
    TOTAL_OPS.append(total_ops)
    TOTAL_CONFS.append(total_confs)
    TOTAL_TIME.append(total_time)

    with open("C:/Users/OMEN/Desktop/Randomized_pre_defined.txt","a") as f:
        f.write("\n\n%Todos os parâmetros")
        f.write("\nSize ="+str(s)+";")
        f.write("\n"+"Ks ="+ str(k_tentados)+";")
        f.write("\n"+"Operacoes ="+ str(op_tentados)+";")
        f.write("\n"+"Tempos_tentados ="+ str(times_tentados)+";")
        f.write("\n"+"N_Configurations ="+ str(confs_tentados)+";")

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
    print('Size of dominating set returned by nX function:',len(nX.dominating_set(G)))
    print(nX.dominating_set(G))


if __name__ == "__main__":
   main()
