

def r3(n: int) -> int:
    if(n==0):
        return 0
    return 1 + 2*r3(n-1)

def r4(n: int) -> int:
    if(n==0):
        return 0
    return 1 + r4(n-1) + r4(n-1)

if __name__ == "__main__":
    print(r3(50))
    print(r4(25))