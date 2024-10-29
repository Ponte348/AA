from random import randint

def throw_coin(n):
    heads, tails = 0, 0
    
    for i in range(n):
        if randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    
    return heads, tails
    
def throw_three_coins():
    heads_count = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in range(1000000):
        n = 3
        heads, tails = throw_coin(n)
        heads_count[heads] += 1
    
    return heads_count

def throw_n_coins(n):
    heads_count = {i: 0 for i in range(n+1)}
    for i in range(1000000):
        heads, tails = throw_coin(n)
        heads_count[heads] += 1
    
    return heads_count

def throw_biased_coin(n, p):
    heads, tails = 0, 0
    
    for i in range(n):
        if randint(0, 100) < p*100:
            heads += 1
        else:
            tails += 1
    
    return heads, tails

def throw_n_biased_coins(n, p):
    heads_count = {i: 0 for i in range(n+1)}
    for i in range(1000000):
        heads, tails = throw_biased_coin(n, p)
        heads_count[heads] += 1
    
    return heads_count

def main():
    print()
    
    print("Probabilities for 3 throws:")
    for k, v in throw_three_coins().items():
        print(f"Number of heads: {k}, Probability: {v/1000000*100:.2f}%")

    print()
    
    #print("Probabilities for 10 throws:")
    #for k, v in throw_n_coins(10).items():
    #    print(f"Number of heads: {k}, Probability: {v/1000000*100:.2f}%")
        
    print()

    print("Probabilities for 3 throws with 2/3 of heads:")
    for k, v in throw_n_biased_coins(3, 2/3).items():
        print(f"Number of heads: {k}, Probability: {v/1000000*100:.2f}%")

if __name__ == "__main__":
    main()