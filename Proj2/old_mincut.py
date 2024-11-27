from utils import *
from old_rand_algorithms import *
from time import perf_counter_ns
import numpy as np
import matplotlib.pyplot as plt


def test_randomized_exhaustive_min_cut(n, graph, max_time=60, max_iterations=1000, filename="randomized_exhaustive_min_cut.png"):
    """
    Test the randomized exhaustive algorithm, visualize the min cut, and print results.
    """
    min_cut_weight, min_cut_partition, operations, iterations = randomized_exhaustive_min_cut(
        graph, max_time=max_time, max_iterations=max_iterations)
    print(f"Randomized Exhaustive Results for n={n}:")
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {operations}")
    print(f"Iterations: {iterations}\n")
    
    visualize_min_cut(graph, min_cut_partition, filename)


def test_randomized_greedy_min_cut(n, graph, max_time=60, max_iterations=1000, filename="randomized_greedy_min_cut.png"):
    """
    Test the randomized greedy algorithm, visualize the min cut, and print results.
    """
    min_cut_weight, min_cut_partition, operations, iterations = randomized_greedy_min_cut(
        graph, max_time=max_time, max_iterations=max_iterations)
    print(f"Randomized Greedy Results for n={n}:")
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {operations}")
    print(f"Iterations: {iterations}\n")
    
    visualize_min_cut(graph, min_cut_partition, filename)

def generate_execution_time_plot(algorithm, algorithm_name, node_range, edge_prob, max_time, max_iterations, filename_prefix):
    """
    Generate a plot for execution time vs number of nodes for a given algorithm.
    """
    nodes = []
    times = []
    
    for n in node_range:
        graph = generate_graph_erdos_renyi(n, edge_prob)
        start = perf_counter_ns()
        algorithm(graph, max_time=max_time, max_iterations=max_iterations)
        end = perf_counter_ns()
        time_taken = (end - start) * 1e-9  # Convert to seconds
        nodes.append(n)
        times.append(time_taken)
        print(f"Execution Time for {algorithm_name} with n={n}: {time_taken:.2f} seconds")

        # Stop if time exceeds the max_time
        if time_taken > max_time:
            print(f"{algorithm_name} exceeded time limit for n={n}. Stopping...\n")
            break

    # Plot execution time
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, times, marker='o', label=f"{algorithm_name}")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Execution Time vs Number of Nodes ({algorithm_name})")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename_prefix}_execution_time.png")
    plt.close()


def generate_operations_plot(algorithm, algorithm_name, node_range, edge_prob, max_time, max_iterations, filename_prefix):
    """
    Generate a plot for operations vs number of nodes for a given algorithm.
    """
    nodes = []
    operations_list = []
    
    for n in node_range:
        graph = generate_graph_erdos_renyi(n, edge_prob)
        print(f"Testing {algorithm_name} with n={n}")
        _, _, operations, _ = algorithm(graph, max_time=max_time, max_iterations=max_iterations)
        nodes.append(n)
        operations_list.append(operations)
        print(f"Operations for {algorithm_name} with n={n}: {operations}\n")

    # Plot operations
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, operations_list, marker='o', label=f"{algorithm_name}")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Number of Operations")
    plt.title(f"Operations vs Number of Nodes ({algorithm_name})")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename_prefix}_operations.png")
    plt.close()

"""
def main():
    # Parameters for testing
    max_time = 60  # Maximum time for each algorithm
    max_iterations = 1000  # Maximum iterations for the randomized algorithms
    edge_prob = 0.5  # Probability of edge creation

    # Generate and visualize results for specific graphs
    for n in [10, 15, 20, 100]:
        graph = generate_graph_erdos_renyi(n, edge_prob)
        visualize_and_save_graph(graph, f"erdos_renyi_graph_{n}_nodes.png")
        
        # Test algorithms
        test_randomized_exhaustive_min_cut(n, graph, max_time=max_time, max_iterations=max_iterations,
                                           filename=f"randomized_exhaustive_min_cut_{n}_nodes.png")
        test_randomized_greedy_min_cut(n, graph, max_time=max_time, max_iterations=max_iterations,
                                       filename=f"randomized_greedy_min_cut_{n}_nodes.png")

    # Generate execution time plots for randomized algorithms
    node_range = range(10, 100, 1)  # Range of nodes for testing
    generate_execution_time_plot(randomized_exhaustive_min_cut, "Randomized Exhaustive", node_range, edge_prob,
                                 max_time, max_iterations, "randomized_exhaustive")
    generate_execution_time_plot(randomized_greedy_min_cut, "Randomized Greedy", node_range, edge_prob,
                                 max_time, max_iterations, "randomized_greedy")
    
    # Generate operations plots for randomized algorithms
    generate_operations_plot(randomized_exhaustive_min_cut, "Randomized Exhaustive", node_range, edge_prob,
                             max_time, max_iterations, "randomized_exhaustive")
    generate_operations_plot(randomized_greedy_min_cut, "Randomized Greedy", node_range, edge_prob,
                             max_time, max_iterations, "randomized_greedy")
"""

"""
New algorithms
"""


def test_karger_min_cut(n, graph, iterations=100, filename="karger_min_cut.png"):
    """
    Test Karger's Min-Cut algorithm, visualize the min cut, and print results.
    
    Args:
        n (int): Number of nodes in the graph.
        graph (dict): The graph represented as an adjacency list.
        iterations (int): Number of times to run Karger's algorithm.
        filename (str): Filename for saving the visualization.
    """
    min_cut = run_karger_multiple_times(graph, iterations)
    print(f"Karger's Algorithm Results for n={n}:")
    print(f"Minimum cut found: {min_cut}\n")
    
    # Visualization
    # Note: Since Karger's algorithm doesn't return partitions directly, we can't visualize the cut
    # partitions here. Instead, we just save the original graph visualization.
    visualize_and_save_graph(graph, filename)


def generate_execution_time_plot_karger(node_range, edge_prob, iterations, filename_prefix):
    """
    Generate a plot for execution time vs number of nodes for Karger's algorithm.
    
    Args:
        node_range (range): Range of nodes to test.
        edge_prob (float): Probability of edge creation in the graph.
        iterations (int): Number of iterations for Karger's algorithm.
        filename_prefix (str): Prefix for the output plot filename.
    """
    nodes = []
    times = []
    
    for n in node_range:
        graph = generate_graph_erdos_renyi(n, edge_prob)
        start = perf_counter_ns()
        run_karger_multiple_times(graph, iterations)
        end = perf_counter_ns()
        time_taken = (end - start) * 1e-9  # Convert to seconds
        nodes.append(n)
        times.append(time_taken)
        print(f"Execution Time for Karger's Algorithm with n={n}: {time_taken:.2f} seconds")

    # Plot execution time
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, times, marker='o', label="Karger's Algorithm")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Number of Nodes (Karger's Algorithm)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename_prefix}_execution_time.png")
    plt.close()


def generate_operations_plot_karger(node_range, edge_prob, iterations, filename_prefix):
    """
    Generate a plot for operations vs number of nodes for Karger's algorithm.
    
    Args:
        node_range (range): Range of nodes to test.
        edge_prob (float): Probability of edge creation in the graph.
        iterations (int): Number of iterations for Karger's algorithm.
        filename_prefix (str): Prefix for the output plot filename.
    """
    nodes = []
    operations_list = []
    
    for n in node_range:
        graph = generate_graph_erdos_renyi(n, edge_prob)
        print(f"Testing Karger's Algorithm with n={n}")
        
        # Since Karger's algorithm doesn't return operations explicitly, we can't track them here.
        # We'll assume each run is a single "operation" for simplicity.
        run_karger_multiple_times(graph, iterations)
        operations = iterations  # Placeholder for operations
        nodes.append(n)
        operations_list.append(operations)
        print(f"Operations for Karger's Algorithm with n={n}: {operations}\n")

    # Plot operations
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, operations_list, marker='o', label="Karger's Algorithm")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Number of Operations")
    plt.title("Operations vs Number of Nodes (Karger's Algorithm)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename_prefix}_operations.png")
    plt.close()

def main():
    # Parameters for testing
    iterations = 100  # Number of iterations for Karger's algorithm
    edge_prob = 0.5  # Probability of edge creation

    # Generate and visualize results for specific graphs
    for n in [10, 15, 20, 100]:
        graph = generate_graph_erdos_renyi(n, edge_prob)
        visualize_and_save_graph(graph, f"erdos_renyi_graph_{n}_nodes.png")
        
        # Test Karger's algorithm
        test_karger_min_cut(n, graph, iterations=iterations, filename=f"karger_min_cut_{n}_nodes.png")

    # Generate execution time plots for Karger's algorithm
    node_range = range(10, 500, 10)  # Range of nodes for testing
    generate_execution_time_plot_karger(node_range, edge_prob, iterations, "karger")

    # Generate operations plots for Karger's algorithm
    generate_operations_plot_karger(node_range, edge_prob, iterations, "karger")

if __name__ == "__main__":
    main()