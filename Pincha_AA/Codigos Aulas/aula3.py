
def main():
    ##### Variaveis 
    global rec_counter
    global rec_alloc
    global rec_linear

    ##### Fibonacci
    print("{:1s}    {:7s}   {:5s}        {:2s}   {:7s}   {:10s}".format("x","fibo(x)","n_chamadas","y","fibo(x)","n_chamadas"))
    for i in range(0,20):
        rec_counter = 0
        rec_alloc = 0
        x = recur_fibo(i)
        y = alloc_fibo(i)
        print("{:2d}    {:7d}  {:10d}       {:2d}   {:7d} {:10d}".format(i,x,rec_counter,i,y,rec_alloc))

    print("\n\n")

    ##### Linear Robot
    print("{:1s}    {:15s}   {:5s}".format("x","linear_robot(x)","n_chamadas"))
    for j in range(1,10):
        rec_linear = 0
        z = linear_robot(j)
        print("{:2d}    {:7d}  {:10d}".format(j,z,rec_linear))

    #### Triangulo de Pascal Recursiva
    triangle = pascals_triangle(5)
    for row in triangle:
        print(row)

    return 0


# Python program to display the Fibonacci sequence

def recur_fibo(n):
    global rec_counter
    if n <= 1:
        return n
    else:
        rec_counter += 1
        return(recur_fibo(n-1) + recur_fibo(n-2))


def alloc_fibo(n):
    global rec_alloc
    # base case
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    # create empty dp array
    dp = [0] * (n + 1)

    # find patterns
    dp[0] = 0
    dp[1] = 1
    
    #print("Pre-generated DP Array = ", dp)
    # dp[2] = dp[1] + dp[0]
    # dp[i] = dp[i-1] + dp[i-2]
    
    for i in range(2,n+1):
        rec_alloc +=1
        dp[i] = dp[i-1] + dp[i-2]
    
    #print("Generated DP Array after filling = ", dp)
    
    return(dp[n])


def linear_robot(n):
    global rec_linear
    if n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        rec_linear += 2
        return(linear_robot(n-1) + linear_robot(n-2) + linear_robot(n-3))
        

def pascals_triangle(n):
    """ Recursive function to calculate Pascals Triangle """
    if n == 1:
        return [[1]] # Base case termination condition
    else:
        result = pascals_triangle(n-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1] # Take from end of result
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result

def KROW(K):                            #defining function with argument.

    """ Pascals Triangle  with 2D Array """

    LIST = []                           # list declare.
    LIST.append([1])                    # first row

    if(K == 1):
        return(LIST[-1])                # return [1] if K = 1.
    LIST.append([1,1])                  # add second row

    if(K == 2):
        return(LIST[-1])                # return [1,1] if K = 2.

    while(len(LIST)!=K):                # iterate till pascal's triangle not form till K rows.
        l = []
        l.append(1)                     # every row starts with 1.

        for i in range(0,len(LIST[-1])-1):
            a = LIST[-1][i]+LIST[-1][i+1]   # sum up two numbers from previous row for the current row's element .
            l.append(a)

        l.append(1)                         # last element of each row will be 1.
        LIST.append(l)                      # forming each row and storing in 2-D LIST.
        
    return(LIST[-1])


main()