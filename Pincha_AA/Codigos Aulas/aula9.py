import random
import math

def toss_coin(treshold = 0.5):
    return 1 if random.random() < treshold else 0

def prob_counter(n=10000,b=2):
   d = {}
   for j in range(n):
      sum = 0
      for i in range(10000):
         sum += toss_coin(1.0/b**sum)
      if sum not in d:
         d[sum] = 1
      else:
         d[sum] += 1
   print(sorted(d.items(),key=lambda x:x[0]))
   d = {key: value / n*100 for key, value in d.items()}
   print(sorted(d.items(),key=lambda x:x[0]))


## Código do stor
def increment_counter(prob=0.5):
    if random.random() < prob:
        return 1

    return 0


def count_events(num_events = 1, b = 2):
    counter_value = 0

    for i in range(num_events):
        counter_value += increment_counter(1.0 / math.pow(b, counter_value))

    return counter_value
##

def recursive_binary(n,k):
    if n==1 and k ==1:
        return 1
    if n==1 and k == 0:
        return 0
    
    if k == n:
        return 1/(2**n-1)*recursive_binary(n-1,n-1)
    
    else:
        return 1/(2**(k-1))*recursive_binary(n-1,k-1) + (1-1/(2**k))*recursive_binary(n-1,k)


def main():
    prob_counter(1000,2)
    #recursive_binary(10,12)

main()

