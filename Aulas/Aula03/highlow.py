import random
from collections import Counter

def guess(attempts, low, high, answer, tentative):
    attempts+=1
    if tentative == answer:
        return attempts
    else:
        if tentative < answer:
            return guess(attempts, tentative+1, high, answer, (tentative+1+high)//2)
        else:
            return guess(attempts, low, tentative-1, answer, (low+tentative-1)//2)
    
def mid(ntimes, low, high):
    min, median, mean, max = 0,0,0,0
    guesses = []
    
    for i in range(ntimes):
        answer = random.randint(low, high)
        tentative = (low + high) // 2
        tries = guess(0, low, high, answer, tentative)
        
        if min == 0 or tries < min:
            min = tries
        if max == 0 or tries > max:
            max = tries
        
        mean += tries
        guesses.append(tries)
            
    mean = mean / ntimes
    median = guesses[ntimes//2] if ntimes % 2 == 1 else (guesses[ntimes//2] + guesses[ntimes//2-1]) / 2
    
    return min, median, mean, max, guesses
    
def main():
    low = 1
    high = 1000
    ntimes = 100000
    
    min, median, mean, max, guesses = mid(ntimes, low, high)
    
    # count number of occurrences of each element in the list
    counter = Counter(guesses)
    for key, value in sorted(counter.items()):
        print(key,"attempts:", value)
    
    print()
    print("Min: ", min)
    print("Median: ", median)
    print("Mean: ", mean)
    print("Max: ", max)


if __name__ == "__main__":
    main()