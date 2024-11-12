from utils import *
from algorithms import *
from time import perf_counter_ns
import numpy as np
import matplotlib.pyplot as plt

def test_exhaustive_min_cut(n, m_prob, graph, filename="exhaustive_min_cut.png"):
    min_cut_weight, min_cut_partition, exhaustive_operations = exhaustive_min_cut(graph)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {exhaustive_operations}")
    
    visualize_min_cut(graph, min_cut_partition, filename)

def test_greedy_min_cut(n, m_prob, graph, filename="greedy_min_cut.png"):
    min_cut_weight, min_cut_partition, greedy_operations = greedy_min_cut(graph)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {greedy_operations}")
    
    visualize_min_cut(graph, min_cut_partition, filename)

def test_exhaustive():
    print("\n{:<6} {:<8} {:<15} {:<15} {:<15}".format(
        "Nodes", "Prob", "Min Cut Weight", "Operations", "Time (s)"))
    print("-" * 65)

    for n in range(2, 21):
        for p in np.arange(0.1, 1.0, 0.1):
            graph = generate_graph_erdos_renyi(n, p)
            start = perf_counter_ns()
            min_cut_weight, min_cut_partition, operations = exhaustive_min_cut(graph)
            end = perf_counter_ns()
            time_taken = (end - start) * 1e-9
            
            print("{:<6} {:<8.1f} {:<15} {:<15} {:<15.3f}".format(
                n, p, min_cut_weight, operations, time_taken))
        print("-" * 65)  # separator between different node counts

if __name__ == "__main__":
    # For n = 7, 13 and 20 calculate exhaustive search and save the graph figure
    p = 0.75
    for n in [7, 13, 20]:
        graph = generate_graph_erdos_renyi(n, p)
        test_exhaustive_min_cut(n, p, graph, f"exhaustive_min_cut_{n}_nodes.png")