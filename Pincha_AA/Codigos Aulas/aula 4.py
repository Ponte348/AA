from cmath import rect


def delannoy_numbers_recursive(n,m):
    if (n==0) or (m==0):
        return 1

    else:
        return delannoy_numbers_recursive(n-1,m) + delannoy_numbers_recursive(n,m-1) + delannoy_numbers_recursive(n-1,m-1)


def Delannoy_dp(n, m):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    # Base cases
    for i in range(m):
        dp[0][i] = 1
     
    for i in range(1, m + 1):
        dp[i][0] = 1
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + dp[i][j - 1];
 
    return dp[m][n]


def coin_row_dp(coins):
    size = len(coins)
    if size == 0:
        return 0

    elif size == 1:
        return coins[0]

    elif size == 2:
        return max(coins[0],coins[1])
    else:
        F = [0 for j in range(size+1)]
        F[0] = 0; F[1] = coins[0]

        for i in range(2,size+1):
            F[i] = max(coins[i-1] + F[i-2], F[i-1])
        
        return F, rec


def coins_recursive(coins):
    n = len(coins)
    if n ==0:
        return 0
    elif n == 1:
        return coins[0]
    
    antigo = coins_recursive(coins,n-1)
    novo = coins_recursive(coins,n-2) + coins[n-1]
    if antigo > novo:
        return antigo
    else:
        return novo


def main():
    #for i in range(2,10):
        #print("i:",i, "r:", delannoy_numbers_recursive(i,i))
    #print(delannoy_numbers_recursive(15,15))
    #for i in range(1000):
        #print("i:",i, "r:", Delannoy_dp(i,i))

    c = [5,1,2,10,6,2]
    F = coins_recursive(c)
    print(F)


    return 0


main()
