import random

def toss_coin():
    return random.randint(0,1)


def main_toss():
    lst = {}
    n = 100000
    m = 15
    for i in range(n):
        L = []
        for j in range(m):
            c = toss_coin()
            L.append(c)
        d = sum(L)
        if d in lst:
            lst[d] += 1
        else:
            lst[d] = 1


    print()
    print(m,' throws,',n,'times')
    print(sorted(lst.items(),key=lambda x:x[0]))
    prob = {key: (value / n) for key, value in lst.items()}
    print(sorted(prob.items(),key=lambda x:x[0]))
    print()


def stop_tossing(N = 100000):
    dict = {}
    for i in range(N):
        lst = []
        toss = 1
        while True:
            moeda = toss_coin()
            if moeda in lst:
                break
            lst.append(moeda)
            toss += 1
        if toss in dict:
            dict[toss] += 1
        else:
            dict[toss] = 1
    print(sorted(dict.items(),key=lambda x:x[0]))
    prob = {key: (value / N)*100 for key, value in dict.items()}
    print(sorted(prob.items(),key=lambda x:x[0]))
    print()

def trowh_dice():
    return random.randint(1,6)

def stop_tossing_dice(N = 100000):
    dict = {}
    for i in range(N):
        lst = []
        toss = 1
        while True:
            moeda = trowh_dice()
            if moeda in lst:
                break
            lst.append(moeda)
            toss += 1
        if toss in dict:
            dict[toss] += 1
        else:
            dict[toss] = 1
    print(sorted(dict.items(),key=lambda x:x[0]))
    prob = {key: round((value / N)*100,3) for key, value in dict.items()}
    print(sorted(prob.items(),key=lambda x:x[0]))
    print()


def birthday():
    return random.randint(1,365)


def stop_birthday(N = 1000):
    dict = {}
    for i in range(N):
        lst = []
        toss = 1
        while True:
            day = birthday()
            if day in lst:
                break
            lst.append(day)
            toss += 1
        if toss in dict:
            dict[toss] += 1
        else:
            dict[toss] = 1
    print(sorted(dict.items(),key=lambda x:x[0]))
    prob = {key: round((value / N)*100,3) for key, value in dict.items()}
    print('\nProbabilidades:')
    print(sorted(prob.items(),key=lambda x:x[0]))
    print()

# stop after all items have appered at least once
def pruned_coin(n=6,N=200):
    dict = {}
    keyList = range(1,n+1)
    for i in range(N):
        toss = 1
        lst = {key: 0 for key in keyList}
        while True:
            moeda = random.randint(1,n)
            lst[moeda] += 1
            toss += 1
            if(0 not in lst.values()):
                break
        if toss in dict:
            dict[toss] += 1
        else:
            dict[toss] = 1
    print(sorted(dict.items(),key=lambda x:x[0]))
    dict = {key: value / N *100 for key, value in dict.items()}
    print(sorted(dict.items(),key=lambda x:x[0]))



def main():
    #print("Count the number of heads in n throws")
    #main_toss()
    #print("\n Tossing coin, stopping when a face repeats")
    #stop_tossing()
    #print("\n Tossing dice, stopping when a face repeats")
    #stop_tossing_dice()
    #print("\n Choosing Birthday, stop when day repeats")
    #stop_birthday()
    print("\n Stop after all items have appered at least once")
    pruned_coin()


main()