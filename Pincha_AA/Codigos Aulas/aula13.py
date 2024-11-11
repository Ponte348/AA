

path = "C:/Users/OMEN/OneDrive - Universidade de Aveiro/Mestrado/4 ano/1 semestre/AA/Sugestões de Leitura/Aula 13"
file = "aleatorios000002500.txt"

def get_list(path,file): 
    with open(path+"/"+file, "r", encoding="utf8") as f:
        # add elements from file to list
        input_list = [int(line) for line in f]

    return input_list

def bit_map(input_list):
    lst = []
    for i in range(len(input_list)):
        if input_list[i] not in lst:
            input_list[i] = 1
            lst.append(input_list[i])

    return len(lst)


def count_unite(input_list):
    input_list.sort()
    count = 1

    for i in range(1,len(input_list)):
        if input_list[i] != input_list[i-1]:
            count += 1
    
    return count

def main():
    list = get_list(path,file)
    input_list = count_unite(list)
    print('Nº diferentes: ',input_list,'\n')

    bit_list = bit_map(list)
    print('Nº diferentes: ',bit_list,'\n')

main()