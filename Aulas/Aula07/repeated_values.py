from random import randint

# generate random numbers (with interval [0, n]) until you get a repeated one
def repeated(n):
    numbers = dict()
    count = 0
    while True:
        count+=1
        r = randint(0, n)
        if r in numbers:
            return count
        numbers[r] = True

def main():
    n = 4000
    repetitions = 1000000
    sum=0

    for j in range(repetitions):
        c = repeated(n)
        sum+=c
        print("\r", j+1, end="")

    print("\nAverage number of random numbers generated until a repeated one:", sum/repetitions, "\n")

if __name__ == "__main__":
    print()
    main()