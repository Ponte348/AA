def f1(n: int) -> int:
    i, r, g = 0, 0, 0
    for i in range(1, n+1):
        r += i
        g+=1
    return (r, g)

def f2(n: int) -> int:
    i,j,r, g = 0,0,0,0
    for i in range(1, n+1):
        for j in range(1, n+1):
            r += 1
            g+=1
    return (r, g)

def f3(n: int) -> int:
    i,j,r,g = 0,0,0,0
    for i in range(1, n+1):
        for j in range(i, n+1):
            r += 1
            g+=1
    return (r, g)

def f4(n: int) -> int:
    i,j,r,g = 0,0,0,0
    for i in range(1, n+1):
        for j in range(1, i+1):
            r += j
            g+=1
    return (r, g)

if __name__ == "__main__":
    #print("f1(10) = ", f1(10))
    #print("f2(10) = ", f2(10))
    #print("f3(10) = ", f3(10))
    #print("f4(10) = ", f4(10))
    
    # test for n values 1 to 10 and count g, number of iterations
    for n in range(1, 11):
        print("f1({}) = {}".format(n, f1(n)))
        print("f2({}) = {}".format(n, f2(n)))
        print("f3({}) = {}".format(n, f3(n)))
        print("f4({}) = {}".format(n, f4(n)))
        print()
    