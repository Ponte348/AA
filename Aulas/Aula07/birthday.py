#Given n people in a room, what is the probability that at least two of them share the same birthday?
def birthday(n):
    p = 1
    for i in range(1, n):
        p *= (365 - i) / 365
    return 1 - p

def main():
    for i in range(1, 366):
        prob = birthday(i)
        print(f"{i} people: {prob*100:.2f}%")
        if prob >= 0.5:
            break
        

if __name__ == "__main__":
    main()