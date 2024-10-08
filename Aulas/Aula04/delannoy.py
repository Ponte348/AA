import functools
from time import perf_counter_ns
import matplotlib.pyplot as plt

def recursion_delannoy(m, n):
    if m == 0 or n == 0:
        return 1
    return recursion_delannoy(m-1, n) + recursion_delannoy(m, n-1) + recursion_delannoy(m-1, n-1)

def twoD_array_delannoy(m, n):
    if m == 0 or n == 0:
        return 1
    matrix = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        matrix[i][0] = 1
    for j in range(n+1):
        matrix[0][j] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] + matrix[i-1][j-1]
    return matrix[m][n]
    
def main(n, method):
    if method == "recursion":
        recursion_taken = []
        for i in range(n+1):
            start = perf_counter_ns()
            print("Delannoy(",i,",",i,"):", recursion_delannoy(i, i), 
                "; Time taken:", round((perf_counter_ns() - start)/1000000000, 2), "s")
            taken = perf_counter_ns() - start
            recursion_taken.append(taken)
            if (taken > 1000000000):
                print("It's taking too much time!")
                break
        
        plt.plot(range(len(recursion_taken)), recursion_taken, marker='o', label='Recursion Time')
        plt.xlabel('n')
        plt.ylabel('Time (seconds)')
        plt.title('Recursion Time for Delannoy Numbers')
        plt.legend()
        plt.grid(True)
        # Save the plot to a file
        plt.savefig('recursion_delannoy_plot.png')  # Save the plot as a PNG image
        print("Plot saved as 'recursion_delannoy_plot.png'")
        
    elif method == "2D array":
        twoD_array_taken = []
        for i in range(n+1):
            start = perf_counter_ns()
            print("Delannoy(",i,",",i,"):", twoD_array_delannoy(i, i), 
                "; Time taken:", round((perf_counter_ns() - start)/1000000000, 2), "s")
            taken = perf_counter_ns() - start
            twoD_array_taken.append(taken)
            if (taken > 1000000000):
                print("It's taking too much time!")
                break
        
        plt.plot(range(len(twoD_array_taken)), twoD_array_taken, marker='o', label='2D Array Time')
        plt.xlabel('n')
        plt.ylabel('Time (seconds)')
        plt.title('2D Array Time for Delannoy Numbers')
        plt.legend()
        plt.grid(True)
        # Save the plot to a file
        plt.savefig('2D_array_delannoy_plot.png')
        print("Plot saved as '2D_array_delannoy_plot.png'")

    elif method == "two 1D arrays":
        two_1D_arrays_taken = []
        for i in range(n+1):
            start = perf_counter_ns()
            print("Delannoy(",i,",",i,"):", two_1D_arrays_delannoy(i, i), 
                "; Time taken:", round((perf_counter_ns() - start)/1000000000, 2), "s")
            taken = perf_counter_ns() - start
            two_1D_arrays_taken.append(taken)
            if (taken > 1000000000):
                print("It's taking too much time!")
                break
        
        plt.plot(range(len(two_1D_arrays_taken)), two_1D_arrays_taken, marker='o', label='Two 1D Arrays Time')
        plt.xlabel('n')
        plt.ylabel('Time (seconds)')
        plt.title('Two 1D Arrays Time for Delannoy Numbers')
        plt.legend()
        plt.grid(True)
        # Save the plot to a file
        plt.savefig('two_1D_arrays_delannoy_plot.png')
        print("Plot saved as 'two_1D_arrays_delannoy_plot.png'")
if __name__ == "__main__":
    # ask user for input
    method = input("Enter the method you want to use (recursion, 2D array, two 1D arays, memoization): ")
    n = int(input("Enter a number: "))
    print()
    main(n, method)