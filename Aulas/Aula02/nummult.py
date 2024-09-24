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


if __name__ == "__main__":
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