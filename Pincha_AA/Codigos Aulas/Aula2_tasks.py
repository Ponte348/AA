def iterative(a,b):
    answer = 1
    mult = 0
    for i in range(b):
        mult += 1
        answer = answer * a
    return answer, mult

def recursion_dumb(a,b):
    global counter_recursion_dumb
    global c_rec_dumb
    if b == 0:
        return 1
    else:
        counter_recursion_dumb += 1
        c_rec_dumb += 1
        return a*recursion_dumb(a,b-1)

def recursion_div(a,b):
    global counter_recursion_div
    global c_rec_div 
    if b == 0:
        return 1
    elif b == 1:
        return a
    p = recursion_div(a,(b)//2)
    if b%2 == 0:
        counter_recursion_div += 1
        c_rec_div += 1
        return p*p
    else:
        counter_recursion_div += 2
        c_rec_div += 2
        
        return a * p * p

def divide_and_conquer(a,b):
    global div_count
    if b==0:
        return 1
    elif b==1:
        return a
    div_count += 1
    return divide_and_conquer(a,b//2)*divide_and_conquer(a,(b+1)//2)

def main():
    a=2
    global counter_recursion_dumb
    global counter_recursion_div

    global c_rec_dumb 
    global c_rec_div 

    global div_count
    print("{:3s} {:7s} {:9s} {:7s} {:9s} {:3s} {:7s} {:9s} {:3s} {:7s}".format("n","valor_1","n_mult_1","valor_2","n_mult_2","rec_2","valor_3","n_mult_3","rec_3","div&conquer"))
    for b in range(0,9):
        counter_recursion_dumb = 0
        counter_recursion_div = 0
        c_rec_dumb = 0
        c_rec_div = 0
        div_count = 0
        a1, counter_mult = iterative(a,b)
        a2 = recursion_dumb(a,b)
        a3 = recursion_div(a,b)
        a4=divide_and_conquer(a,b)
        print("{:3d} {:7d} {:9d} {:7d} {:9d} {:3d} {:7d} {:9d} {:3d} {:7d}".format(b,a1,counter_mult,a2,counter_recursion_dumb,c_rec_dumb,a3,counter_recursion_div,c_rec_div,div_count))



if __name__ == "__main__":
   main()