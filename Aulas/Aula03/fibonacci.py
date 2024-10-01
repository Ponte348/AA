from time import perf_counter_ns
import functools

operation_count = 0

# This uses python's lru_cache to store the results of the function
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    global operation_count
    if n == 0:
        return 0
    if n == 1:
        return 1
    operation_count += 1
    return fibonacci(n-1) + fibonacci(n-2)

memo = {}
def dynamicfibonacci(n):
    global operation_count
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    operation_count += 1
    memo[n] = dynamicfibonacci(n-1) + dynamicfibonacci(n-2)
    return memo[n]

def main():
    for i in range(10000+1):
        global operation_count, memo
        operation_count = 0
        start = perf_counter_ns()
        print("Fibonacci(",i,"):", fibonacci(i))
        print("Time:", round((perf_counter_ns() - start)/1000000000, 2), "s; Operations:", operation_count)
        print()
        
        if(perf_counter_ns() - start > 1000000000):
            print("It's taking too much time!")
            break

if __name__ == "__main__":
    main()