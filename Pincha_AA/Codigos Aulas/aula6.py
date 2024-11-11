import random


def toss_coin(treshold = 0.5):
    return 1 if random.random() < treshold else 0

def trowh_dice():
    return random.randint(1,6)

def trowh_dice_biased():
    sequence = [1,1,2,3,4,5,6] # 1 tem uma maior probabilidade (2/7) todos os outros tem (1/7)
    return sequence[random.randrange(len(sequence))]


def main_coin_toss():
    for i in [1000,10000,100000,1000000,10000000]:
        heads = 0
        tails = 0

        for j in range(i):
            a = toss_coin()
            if a == 1:
                heads = heads + 1
            else:
                tails = tails + 1
        print('\nRepeting the experiment',i,' times')
        print('Heads: ', heads,' - ', round((heads/i)*100,2),' %')
        print('Tails: ', tails,' - ', round((tails/i)*100,2),' %')

def main_dice_trow():
   for i in [100,1000,10000,100000,1000000]:
    lst = {}
    for j in range(i):
        d = trowh_dice()
        if d in lst:
            lst[d] +=1
        else:
            lst[d] =1
    
    print('\nRepeting the experiment',i,' times')
    print(sorted(lst.items(),key=lambda x:x[0]))
    prob = {key: round((value / i)*100,2) for key, value in lst.items()}
    print(sorted(prob.items(),key=lambda x:x[0]))
    print()

def main_dice_trow_biased():
   for i in [100,1000,10000,100000,1000000]:
    lst = {}
    for j in range(i):
        d = trowh_dice_biased()
        if d in lst:
            lst[d] +=1
        else:
            lst[d] =1
    
    print('\nRepeting the experiment',i,' times')
    print(sorted(lst.items(),key=lambda x:x[0]))
    prob = {key: round((value / i)*100,2) for key, value in lst.items()}
    print(sorted(prob.items(),key=lambda x:x[0]))
    print()


def simple_game():
    for i in [100,1000,10000,100000,1000000]:
        win = 0
        for j in range(i):
            d_green = trowh_dice()
            d_red = trowh_dice()
            if d_red >= d_green:
                win += 1
        print('\nRepeting the experiment',i,' times')
        print("Nº Wins:",win," - ", round( (win/i)*100, 2),'%')

def simple2_game():
    for i in [100,1000,10000,100000,1000000]:
        guess = random.randint(1,12)
        win = 0
        for j in range(i):
            d_green = trowh_dice()
            d_red = trowh_dice()
            if guess == (d_green+d_red):
                win += 1

        print('\nRepeting the experiment',i,' times')
        print("Nº Wins:",win," - ", round( (win/i)*100, 2),'%')
            



def main():
    print('Coin Problem')
    main_coin_toss()
    print('\nDice Throw Problem')
    main_dice_trow()
    print('\nUnbiased Dice Throw Problem')
    main_dice_trow_biased()
    print('\nSimple Game')
    simple_game()
    print('\n2º Simple Game')
    simple2_game()

main()