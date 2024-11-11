import count_min_sketch as cl
import random
random.seed(20)

def main():
    m = 5 #alterando de 5 para 50 ja ha diferenca nos resultados pelo numero de colisoes
    d = 3
    c = cl.CountMinSketch(m,d)
    c.update(5)
    c.update(5)
    for i in range(90):
        r = random.randint(2,80)
        c.update(r)
    print(c.query(5))

if __name__ == "__main__":
   main()