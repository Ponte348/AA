import lossy_counter as LC
import prob_counter as PC
import exact_counter as EC
import calculate_parameters as CP
import sys

from unidecode import unidecode
import os
import random
import time
random.seed(98012)

# Como vai ser corrido em dois computadores diferentes decidi implementar esta variavel para os paths
# 0 - Omen
# 1 - Asus
pc = 0

def get_paths(pc):
    if pc == 0: # OMEN
        path = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/98012_T3_AA/"
        dirty = path + "dirty_files/"
        clean = path + "clean_files/"
        counter = path +"counter/"
    if pc == 1: # ASUS
        path = "D:/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Trabalho 3/98012_T3_AA/"
        dirty = path + "dirty_files/"
        clean = path + "clean_files/"
        counter = path +"counter/"

    return dirty, clean, counter

def create_output(output_name, parameter_name, n, e):
    with open(output_name,"w") as out:
        out.write("Output file - Gonçalo Freitas (98012)\n")
        out.write('\n')
    
    name = parameter_name+'prob_counter_'+str(n)+".txt"
    with open(name,"w") as out:
        out.write("Ficheiro com métricas -> Probabilistic Counter("+str(n)+") - Gonçalo Freitas (98012)\n")
        out.write('\n')

    name = parameter_name+'exact_counter.txt'
    with open(name,"w") as out:
        out.write("Ficheiro com métricas -> Exact Counter - Gonçalo Freitas (98012)\n")
        out.write('\n')

    name = parameter_name+'lossy_counter_'+str(e)+'.txt'
    with open(name,"w") as out:
        out.write("Ficheiro com métricas -> Lossy Counter("+str(e)+") - Gonçalo Freitas (98012)\n")
        out.write('\n')

    return 0

# create a function that joins all files in 'clean' directory into one file
def join_files(clean):
    with open(clean+"all.txt","w") as out:
        for file in os.listdir(clean):
            with open(clean+file,"r") as f:
                for line in f:
                    out.write(line)



def clean_text(file,dirty,clean):
    input = dirty+file+'.txt'
    output = clean+file+'.txt'
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

                if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:     # O livro/ficheiro vai começar agora
                    begin = True

    print("Done cleaning file - "+file,'\n')
    
    return 0

# Função para fazer print do TOP x mais usadas
def counter_print(counter, file, alg, dic,x, is_new):
    count_file = counter+file+"_"+alg+'.txt'

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
    dirty, clean, counter = get_paths(pc)
    
    dirty_files = os.listdir(dirty)   # obtem todos os ficheiros na pasta 'dirty'
    for i in range(len(dirty_files)):
        dirty_files[i] = dirty_files[i][:-4]
    dirty_files.sort()

    for file in dirty_files:
        clean_text(file,dirty,clean)

    join_files(clean)
    clean_files = os.listdir(clean)   # obtem todos os ficheiros na pasta 'clean'
    for i in range(len(clean_files)):
        # remove o .txt no fim do nome do ficheiro
        clean_files[i] = clean_files[i][:-4]
    clean_files.sort()

    e = 0.01

    n = 100
    k = 3 # para probabilidade 1/8 (1/2^k)

    output_name = counter+'output.txt'
    parameter_name = counter+'metricas_'
    create_output(output_name,parameter_name, n, e)

    exact_time = [0]*len(clean_files)
    prob_time = [0]*len(clean_files)
    lossy_time = [0]*len(clean_files)

    t = 0

    for file in clean_files:

        start = time.time()
        dic_exact = EC.exact_counter(clean,file)
        end = time.time()
        exact_time[t] = end - start
        print("Exact counter time: ",end - start," (s)\n")

        start = time.time()
        dic_prob = PC.probabilistic_counter(n,k,clean,file)
        end = time.time()
        prob_time[t] = end - start
        print("Probabilistic counter time (", str(n),") : ",end - start," (s)\n")

        start = time.time()
        dic_lossy = LC.lossy_counter(e,clean,file)
        end = time.time()
        lossy_time[t] = end - start
        print("Lossy counter time (", str(e),"): ",end - start," (s)\n")

        stdoutOrigin=sys.stdout 
        sys.stdout = open(output_name, "a")

        t+=1

        for dic in (dic_exact, dic_prob, dic_lossy):
            lo = False
            if dic == dic_exact:
                alg = "exact_counter"
            if dic == dic_prob:
                lo = False
                alg = "prob_counter_"+str(n)
                lo = False
            if dic == dic_lossy:
                alg = "lossy_counter_"+str(e)
                dic = {k: v for k, v in dic_lossy.items()}
                lo = True
                
            # print do top 3,5,10 e todas as letras para o respetivo ficheiro
            is_new = 0
            for x in (3,5,10, len(dic)):
                if len(dic) < x: # se tiver menos letras que x, não se faz print
                    pass
                else:
                    counter_print(counter, file, alg, dic, x, is_new)
                    is_new += 1
        
            with(open(parameter_name+alg+".txt","a")) as f:
                if lo == True:
                    dic2 = {k: v[0] for k, v in dic_lossy.items()}  # remove o parâmetro delta para se poder calcular os parâmetros de evaluação de modelo -> usa-se o limite inferior da frequência, f, (ver relatório) para calcular os parâmetros
                    mean, variance, std, max_dev, mad, mse, accuracy, n_true, accuracy_ranking, n_true_ranking = CP.calculate_parameters(dic_exact, dic2)
                else:
                    mean, variance, std, max_dev, mad, mse, accuracy, n_true, accuracy_ranking, n_true_ranking = CP.calculate_parameters(dic_exact, dic)

                # escreve para os ficheiros os parametros de avaliação de modelo
                if alg == "exact_counter":  # se for método de exact counter, não tem exatidão, n_true, exatidão no ranking, n_true no ranking e mse
                    f.write("Ficheiro: "+file+"\n")
                    f.write("Média: "+str(mean)+"\n")
                    f.write("Variância: "+str(variance)+"\n")
                    f.write("Desvio Padrão: "+str(std)+"\n")
                    f.write("Máximo Desvio: "+str(max_dev)+"\n")
                    f.write("Desvio absoluto médio: "+str(mad)+"\n")
                    f.write("Nº letras: "+str(len(dic))+"\n")
                    f.write("Valor máximo do contador: "+str(max(dic.values()))+"\n")
                    f.write("Valor mínimo do contador: "+str(min(dic.values()))+"\n")
                    f.write("Tempo de execução: "+str(exact_time[t-1])+" (s)\n")
                    f.write('\n')

                else:
                    f.write("Ficheiro: "+file+"\n")
                    f.write("Média: "+str(mean)+"\n")
                    f.write("Variância: "+str(variance)+"\n")
                    f.write("Desvio Padrão: "+str(std)+"\n")
                    f.write("Máximo Desvio: "+str(max_dev)+"\n")
                    f.write("Desvio absoluto médio: "+str(mad)+"\n")
                    f.write("Erro quadrático médio: "+str(mse)+"\n")
                    f.write("Exatidão em contadores: "+str(accuracy)+" %\n")
                    f.write("Número de contadores com valores corretos: "+str(n_true)+"\n")
                    f.write("Exatidão Ranking de letras: "+str(accuracy_ranking)+" %\n")
                    f.write("Número de posições corretas no ranking: "+str(n_true_ranking)+"\n")
                    f.write("Nº letras: "+str(len(dic))+"\n")
                    f.write("Valor máximo do contador: "+str(max(dic.values()))+"\n")
                    f.write("Valor mínimo do contador: "+str(min(dic.values()))+"\n")
                    if alg == "prob_counter_"+str(n):
                        f.write("Tempo de execução: "+str(prob_time[t-1])+" (s)\n")
                    else:
                        f.write("Tempo de execução: "+str(lossy_time[t-1])+" (s)\n")

                    f.write('\n')


main()