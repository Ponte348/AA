from rand_algorithms import karger_min_cut, run_karger_multiple_times, stoer_wagner_min_cut
from utils import generate_graph_erdos_renyi, visualize_and_save_graph
from time import perf_counter
import matplotlib.pyplot as plt


def test_algorithms(graph_sizes, edge_probability, iterations=100, output_prefix="mincut_results"):
    """
    Test Karger's and Stoer-Wagner algorithms for different graph sizes.
    Saves results of solved graphs and plots execution time/operations.

    Args:
        graph_sizes (list): List of graph sizes (number of nodes) to test.
        edge_probability (float): Probability of edge creation for Erdos-Renyi graphs.
        iterations (int): Number of iterations for Karger's algorithm.
        output_prefix (str): Prefix for saving the results (graphs and plots).
    """
    # Results storage
    karger_times = []
    karger_operations = []
    stoer_times = []
    stoer_operations = []
    nodes = []

    for n in graph_sizes:
        print(f"Testing with graph size: {n}")
        nodes.append(n)

        # Generate a random graph
        graph = generate_graph_erdos_renyi(n, edge_probability)
        visualize_and_save_graph(graph, f"{output_prefix}_original_graph_{n}_nodes.png")

        # Test Karger's Algorithm
        print(f"Running Karger's Algorithm on graph with {n} nodes...")
        start_time = perf_counter()
        min_cut_karger, execution_time_karger, operations_karger = run_karger_multiple_times(graph, iterations)
        end_time = perf_counter()
        karger_times.append(execution_time_karger)
        karger_operations.append(operations_karger)

        print(f"Karger's Algorithm Results for n={n}:")
        print(f"Minimum Cut: {min_cut_karger}")
        print(f"Execution Time: {execution_time_karger:.4f} seconds")
        print(f"Operations Count: {operations_karger}\n")

        # Test Stoer-Wagner Algorithm
        print(f"Running Stoer-Wagner Algorithm on graph with {n} nodes...")
        start_time = perf_counter()
        min_cut_stoer, operations_stoer = stoer_wagner_min_cut(graph)
        end_time = perf_counter()
        execution_time_stoer = end_time - start_time
        stoer_times.append(execution_time_stoer)
        stoer_operations.append(operations_stoer)

        print(f"Stoer-Wagner Algorithm Results for n={n}:")
        print(f"Minimum Cut: {min_cut_stoer}")
        print(f"Execution Time: {execution_time_stoer:.4f} seconds")
        print(f"Operations Count: {operations_stoer}\n")

    # Generate and save execution time plot
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, karger_times, marker='o', label="Karger's Algorithm")
    plt.plot(nodes, stoer_times, marker='s', label="Stoer-Wagner Algorithm")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Number of Nodes")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_execution_time_plot.png")
    plt.close()

    # Generate and save operations count plot
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, karger_operations, marker='o', label="Karger's Algorithm")
    plt.plot(nodes, stoer_operations, marker='s', label="Stoer-Wagner Algorithm")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Operations Count")
    plt.title("Operations Count vs Number of Nodes")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_operations_plot.png")
    plt.close()


def main():
    """
    Main function to test the minimum cut problem using Karger's and Stoer-Wagner algorithms.
    """
    graph_sizes = [10, 20, 50, 100, 200]  # Different graph sizes to test
    edge_probability = 0.5  # Probability of edge creation in Erdos-Renyi graphs
    iterations = 100  # Number of iterations for Karger's algorithm

    test_algorithms(graph_sizes, edge_probability, iterations, output_prefix="mincut")


if __name__ == "__main__":
    main()