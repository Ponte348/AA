import networkx as nX
import matplotlib.pyplot as plt
from math import floor
import random
from itertools import combinations
import time
import numpy as np

def generate_graph(s,p):
    graph = nX.fast_gnp_random_graph(s,p,seed = 98012, directed = False)

    return graph

def prints(G):
    print("\n\n")
    print("Edges:")
    print(nX.edges(G))
    print("Nodes:")
    print(nX.nodes(G))
    print("Dominating set:")
    print(nX.dominating_set(G))
    #print("Matrix:")
    #print(nX.to_numpy_matrix(G))

def coordinates(s):

    coord = [[0 for x in range(2)] for x in range(s)]

    for i in range(s):
        coord[i][0] = random.randint(0,20)
        coord[i][1] = random.randint(0,20)


    return coord

def heuristc(s,k,G):
    global comp_heuristic
    comp_heuristic = 0


    edges_list = list(nX.edges(G))
    #print("\nEdges List:",edges_list)

    vert = []

    for n in range(s):
        vert.append(n)          # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]
    

    S = []  # Dominating Set 

    #G_save = G.copy()

    Length = floor(s*k)

    #if (len(edges_list)==0):
        #return []

    #else:
    result =  [0 for x in range(s)]

    for q in range(len(vert)):
        Vert = vert[q]                      # Vertice 'q'
        K = list(G.neighbors(Vert))
        
        if len(S) == 0:
            S.append(Vert)
            comp_heuristic = comp_heuristic + 1
            #Adicionar Vertice
            
        elif len(S) > 0:
            if np.isin(K, S).sum()>0:
                comp_heuristic = comp_heuristic + 1
                #Não Adicionar Vertice
            else:
                S.append(Vert)
                comp_heuristic = comp_heuristic + 1
                #Adicionar Vertice

            
            if Vert not in S:
                if any(i in K for i in S):
                    comp_heuristic = comp_heuristic + 1
                    result[q] = 1
                else:
                    comp_heuristic = comp_heuristic + 1
                    result[q] = -1

    if -1 not in result and (len(S)==Length):
        comp_heuristic = comp_heuristic + 1
        return S 


    return []


def exaustive(s,k,G):
    global comp_exaustive
    comp_exaustive = 0

    edges_list = list(nX.edges(G))

    #Solutions = []
    #n_solutions = 0        # se se quiser contar o nº de soluções

    G_save = G.copy()

    vert = []
    for n in range(s):
        vert.append(n)          # list com todos os nº de vertices possiveis -> [0,1,2,3,...,s]

    edges = list(nX.edges(G))
    edges = [set(edge) for edge in edges]

    Length = floor(s*k)
    #print("Comprimento do dominating set tem que ser:", Length)

    list_combinations = []
    for n in range(len(vert) + 1): # start loop at 1 to remove the empty tuple
        for comb in combinations(vert, n):
            if not any(edge.issubset(comb) for edge in edges):      # Dentro das combinações possiveis apartir dos vertices ver aquelas que são possiveis para o dominating set
                comp_exaustive = comp_exaustive + 1
                if len(comb) == Length:
                    list_combinations.append(comb)
                    comp_exaustive = comp_exaustive + 1 
                
   #print("Combiantions",list_combinations)
    n_comb = len(list_combinations)

    if n_comb == 0:     # se n ha nenhum set q pode ser dominating set
        comp_exaustive = comp_exaustive + 1
        return []

    for a in range(n_comb):
        S = list(list_combinations[a])                                # vai iterando e vendo a combinação
        result =  [0 for x in range(s)]
        for c in range(len(vert)):
            check = vert[c]
            K = list(G.neighbors(check))
            if check not in S:
                comp_exaustive = comp_exaustive + 1
                if any(i in K for i in S):
                    comp_exaustive = comp_exaustive + 1
                    result[c] = 1
                else:
                    comp_exaustive = comp_exaustive + 1
                    result[c] = -1

        if -1 not in result:
            comp_exaustive = comp_exaustive + 1
            return S


    return []


def main():
    global comp_exaustive
    global comp_heuristic

    P = 0.75
    k = 0.75
    s = 27

    #P_list = [0.75]
    #K = [0.5]
    #S = [5]
        
    coord = coordinates(s)

    print("N vertice:",s, "\nk = ", k)
    print("Comprimento do dominating set tem que ser:", floor(s*k))

    G = generate_graph(s,P)
    print("Dominating set:")
    print(nX.dominating_set(G))

    tic = time.perf_counter()
    
    S_H = heuristc(s,k,G)
    print("\nHeuristic Result:",set(S_H))

    toc = time.perf_counter()
    print(f"Time: {toc - tic:0.4f} seconds")
    #print("Comparações:", comp_heuristic)


    tic = time.perf_counter()

    G = generate_graph(s,P)
    S_E = exaustive(s,k,G)
    print("\nExaustive Result:",set(S_E))
    toc = time.perf_counter()
    print(f"Time: {toc - tic:0.4f} seconds")
    #print("Comparações:", comp_exaustive)
    



if __name__ == "__main__":
   main()