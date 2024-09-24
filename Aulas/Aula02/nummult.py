import math

""" Compute a^b """

# Brute Force - Iterative
def mult1(a: int, b: int) -> int:    
    x = 1
    n = 0
    for i in range(b):
        x = x*a
        n += 1
    return x, n

# Brute Force - Recursive
def mult2(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * mult2(a, b-1)

# Divide and Conquer - Recursive
def mult3(a: int, b: int) -> int:
    global n_count
    n_count += 1
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return mult3(a, b/2) * mult3(a, b/2)
    else:
        return mult3(a, b//2) * mult3(a, math.ceil(b/2))

# Decrease and Conquer - Recursive
def mult4(a: int, b: int) -> int:
    if b == 0:
        return 1
    if b == 1:
        return a
    
    if b % 2 == 0:
        return mult4(a, b/2) * mult4(a, b/2)
    else:
        return a * mult4(a, (b-1)/2) * mult4(a, (b-1)/2)

if __name__ == "__main__":
    # Base value
    a = 2
    
    # Test mult1 with b values from 0 to 10
    print("Brute Force - Iterative, 2^b")
    for i in range(11):
        x,n = mult1(a, i)
        print("b = ", i, " Result: ", x, " Number of calls: ", n)
        
    print("\nBrute Force - Recursive, 2^b")
    # Test mult2 with b values from 0 to 10
    for i in range(11):
        print("b = ", i, " Result: ", mult2(a, i), " Number of calls: ", i)
        
    print("\nDivide and Conquer - Recursive, 2^b")
    # Test mult3 with b values from 0 to 10
    for i in range(11):
        n_count = 0
        print("b = ", i, " Result: ", mult3(a, i), " Number of calls: ", n_count)
    
    print("\nDecrease and Conquer - Recursive, 2^b")
    # Test mult4 with b values from 0 to 10
    for i in range(11):
        num_calls = int(bin(i)[3:].count('1'))*2 + int(bin(i)[3:].count('0'))
        print("b = ", i, " Result: ", mult4(a, i), " Number of calls: ", num_calls)