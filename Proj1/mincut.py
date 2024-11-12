from utils import *
from algorithms import *
from time import perf_counter_ns
import numpy as np
import matplotlib.pyplot as plt

def visualize_min_cut(G, partition, filename="min_cut_graph.png"):
    plt.figure(figsize=(10,10))
    pos = nx.spring_layout(G)
    
    # Draw nodes with different colors for each partition
    set_a, set_b = partition
    nx.draw_networkx_nodes(G, pos, nodelist=set_a, node_color='lightblue', 
                          node_size=500)
    nx.draw_networkx_nodes(G, pos, nodelist=set_b, node_color='lightgreen', 
                          node_size=500)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos)
    
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def test_exhaustive_min_cut(n, m_prob, graph):
    min_cut_weight, min_cut_partition, exhaustive_operations = exhaustive_min_cut(graph)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {exhaustive_operations}")
    
    visualize_min_cut(graph, min_cut_partition, "exhaustive_min_cut.png")

def test_greedy_min_cut(n, m_prob, graph):
    min_cut_weight, min_cut_partition, greedy_operations = greedy_min_cut(graph)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {greedy_operations}")
    
    visualize_min_cut(graph, min_cut_partition, "greedy_min_cut.png")

def main():
    # Lists to store data for plotting
    exhaustive_nodes = []
    exhaustive_ops = []
    exhaustive_times = []
    
    greedy_nodes = []
    greedy_ops = []
    greedy_times = []

    # Test exhaustive algorithm
    for n in range(2, 1000, 1):
        m_prob = 0.5
        random_graph = generate_graph_powerlaw_cluster(n, 3, 0.5)
        print(f"Testing exhaustive with {n} nodes", end="; ")
        start = perf_counter_ns()
        _, _, ops = exhaustive_min_cut(random_graph)
        end = perf_counter_ns()
        time_taken = (end - start)*1e-9
        
        exhaustive_nodes.append(n)
        exhaustive_ops.append(ops)
        exhaustive_times.append(time_taken)
        
        print(f"Execution time: {time_taken:.2f} seconds")
        if time_taken > 5:
            break

    # Test greedy algorithm
    for n in range(2, 1000, 1):
        m_prob = 0.5
        random_graph = generate_graph_powerlaw_cluster(n, 3, 0.5)
        print(f"Testing greedy with {n} nodes", end="; ")
        start = perf_counter_ns()
        _, _, ops = greedy_min_cut(random_graph)
        end = perf_counter_ns()
        time_taken = (end - start)*1e-9
        
        greedy_nodes.append(n)
        greedy_ops.append(ops)
        greedy_times.append(time_taken)
        
        print(f"Execution time: {time_taken:.2f} seconds")
        if time_taken > 1:
            break

    # Create plots
    plt.figure(figsize=(15, 5))
    
    # Operations plot
    plt.subplot(1, 2, 1)
    plt.plot(exhaustive_nodes, exhaustive_ops, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_ops, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations')
    plt.title('Operations vs Number of Nodes')
    plt.legend()
    plt.grid(True)
    
    # Time plot
    plt.subplot(1, 2, 2)
    plt.plot(exhaustive_nodes, exhaustive_times, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_times, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Number of Nodes')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('algorithm_comparison.png')
    plt.close()

    # Also create log-scale plots
    plt.figure(figsize=(15, 5))
    
    # Operations plot (log scale)
    plt.subplot(1, 2, 1)
    plt.plot(exhaustive_nodes, exhaustive_ops, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_ops, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations (log scale)')
    plt.title('Operations vs Number of Nodes (Log Scale)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    
    # Time plot (log scale)
    plt.subplot(1, 2, 2)
    plt.plot(exhaustive_nodes, exhaustive_times, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_times, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds, log scale)')
    plt.title('Execution Time vs Number of Nodes (Log Scale)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    
    plt.tight_layout()
    plt.savefig('algorithm_comparison_log.png')
    plt.close()

if __name__ == "__main__":
    main()