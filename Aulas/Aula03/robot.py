import functools
from time import perf_counter_ns

operation_count = 0

#@functools.lru_cache(maxsize=None)
def robot(n):
    global operation_count
    if n == 0:
        return 1
    if n < 0:
        return 0
    operation_count += 1
    return robot(n-1) + robot(n-2) + robot(n-3)


def main():
    n = 30
    
    for i in range(n+1):
        global operation_count
        operation_count = 0
        start = perf_counter_ns()
        print("Robot(",i,"):", robot(i), 
              "\nOperation count:", operation_count, "; Time taken:", round((perf_counter_ns() - start)/1000000000, 2), "s")
        if (perf_counter_ns() - start > 1000000000):
            print("It's taking too much time!")
            break

if __name__ == "__main__":
    main()