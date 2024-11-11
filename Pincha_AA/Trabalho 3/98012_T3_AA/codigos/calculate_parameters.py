from unidecode import unidecode
import os
import random
import time
import math

random.seed(98012)

def calculate_parameters(dic_exact, dic):
    # ordena os dicionarios pela valor da key
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}                # dicionario que se pretende analisar
    dic_exact = {k: v for k, v in sorted(dic_exact.items(), key=lambda item: item[1], reverse=True)}    # dicionario com valores exatos, retornado pelo exact counter

    # calcula a media
    mean = 0
    for key, value in dic.items():
        mean += value
    mean = mean/len(dic)

    # calcula a variancia
    variance = 0
    for key, value in dic.items():
        variance += (value - mean)**2
    variance = variance/len(dic)

    # calcula o desvio padrao
    std = math.sqrt(variance)

    # calcula o maximo (absoluto) desvio (da média)
    max_dev = 0
    for key, value in dic.items():
        if abs(value - mean) > max_dev:
            max_dev = abs(value - mean)


    # calcula o desvio absoluto médio
    mad = 0
    for key, value in dic.items():
        mad += abs(value - mean)
    mad = mad/len(dic)

    # calcula o erro quadratico medio
    mse = 0
    for key, value in dic_exact.items():
        if key not in dic:      # se a letra não estiver no ranking assume-se q a frequencia é 0
            mse += value**2
        else:
            mse += (value - dic[key])**2
    mse = mse/len(dic)


    # vê se o valor dos contadores são os mesmos
    n_true = 0
    for key, value in dic.items():
        if value == dic_exact[key]:
            n_true += 1
    
    # Exatidão (accuracy) dos valores
    accuracy = (n_true / len(dic_exact)) * 100          # exatidão considerando todos os valores, para as letras não retornadas, considera-se que o valor do seu contador é 0



    # vê se a posição das letras no ranking é a mesma
    n_true_ranking = 0
    for i in range(len(dic)):
        if list(dic.keys())[i] == list(dic_exact.keys())[i]:
            n_true_ranking += 1

    # Exatidão (accuracy) do ranking
    accuracy_ranking = (n_true_ranking / len(dic)) * 100


    return mean, variance, std, max_dev, mad, mse, round(accuracy,2), n_true, round(accuracy_ranking,2), n_true_ranking