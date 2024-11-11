def func1(n):
    r=0
    counter = 0
    for i in range(1,n+1):
        r+=i
        counter+=1
    return n,r,counter

def func2(n):
    r=0
    counter = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            r+=1
            counter+=1
    return n,r, counter

def func3(n):
    r=0
    counter = 0
    for i in range(1,n+1):
        for j in range(i,n+1):
            r+=1
            counter+=1
    return n,r,counter

def func4(n):
    r=0
    counter=0
    for i in range(1,n+1):
        for j in range(i+1):
            r+=j
            counter+=1
    return n,r,counter
print("\n")
for i in range(1,11):
    print(func1(i))

print("\n")

#################################################################################################################

print("R1:")
def r1(n):
    if n==0:
        return 0
    else: 
        return 1+r1(n-1)

print(r1(21))

print("R2:")
def r2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else: 
        return 1+r2(n-2)

print(r2(21))

print("R3:")
def r3(n):
    if n==0:
        return 0
    else: 
        return 1+2*r3(n-1)

print(r2(21))

import time
tic = time.perf_counter()


print("R4:")
def r4(n):
    if n==0:
        return 0
    else: 
        return 1+r4(n-1)+r4(n-1)

print(r4(30))
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")