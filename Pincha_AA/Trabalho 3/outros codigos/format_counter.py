from unidecode import unidecode
import os
import random
import time

# Como vai ser corrido em dois computadores diferentes decidi implementar esta variavel para os paths
# 1 - Omen
# 2 - Asus
pc = 1

def get_paths(pc):
    if pc == 1: #OMEN
        dirty = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/dirty_files/"
        clean = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/clean_files/"
        counter = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/counter/"
    if pc == 0: # ASUS
        dirty = "D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/dirty_files/"
        clean = "D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/clean_files/"
        counter = "D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/counter/"

    return dirty, clean, counter

def clean_text(file,dirty,clean):
    input = dirty+file+".txt"
    output = clean+file+".txt"
    dic = {}

    with open(input,"r", encoding='utf8') as inp:
        with open(output,"w") as out:
            line = inp.readline()
            begin = False # para se tentar limpar ao maximo aquela parte inicial

            while "End of Project Gutenberg" not in line:   # Enquanto não chega ao fim
                line = inp.readline()

                if "End of the Project Gutenberg EBook" in line:
                    begin = False
                    break                                   # Chegou ao fim, break para parar

                if begin == True:                           # Begin = True quer dizer que se pode começar a analisar o texto
                    for i in [*line.strip()]:
                        character = unidecode(i).upper()    # Por tudo para uppercase

                        if character.isalpha():             # Se for uma letra
                            out.write(character)            # Escreve-se a letra para o ficheiro clean

                            if character in dic.keys():     # Se ja tiver no dicionário incrementa-se o contador
                                dic[character] += 1
                            else:                           # Se ainda não tiver no dicionário inicializa-se o contador
                                dic[character] = 1

                if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:     # O livro/ficheiro vai começar agora
                    begin = True

    #print("Exact Counter: Done - "+file)
    print("Done")
    #for key, value in sorted(dic.items(), key=lambda x: x[0], reverse=True): # reverse = True - ordem decresente, reverse = False - ordem cresente 
        #print("{} : {}".format(key, value))
    #print("letras - ",len(dic),'\n')
    
    return dic

# Função para fazer print do TOP x mais usadas
def counter_print(counter, file, alg, dic,x, is_new):
    count_file = counter+file+"_"+alg

    if is_new == 0:                         # Inicializar o ficheiro
        v = "w"
    else:                                   # Dar append
        v = "a"

    with open(count_file,v) as f:
        if (len(dic) == x):
            f.write("All \n")
        else:
            f.write("Top "+str(x)+"\n")

        C = 0
        for key, value in sorted(dic.items(), key=lambda x: x[1], reverse=True): # reverse = True - ordem decresente, reverse = False - ordem cresente 
            f.write("{} : {}\n".format(key, value))
            C +=1
            if C == x:
                break

        f.write('\n')



def main():

    k = 10

    dirty, clean, counter = get_paths(pc)

    #for alg in ("exact_counter.txt"):
    alg = "exact_counter.txt"
    for file in ("cesario_verde", "lusiadas", "the_expedition_of_humphry_clinker"):
        print("Algoritmo:", alg," - file -",file)

        #if alg == "exact_counter.txt":
        tic = time.perf_counter()
        dic = clean_text(file,dirty,clean)
        toc = time.perf_counter()
        print(f"Time: {toc - tic:0.4f} seconds")

    is_new = 0
    for x in (3,5,10, len(dic)):
        counter_print(counter, file, alg, dic, x, is_new)
        is_new += 1



main()

#file = nome do ficheiro
#dirty = o caminho de uma pasta que tem os ficheiros originais
#clean = caminho da pasta para meter os ficheiros bonitos