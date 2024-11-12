from algorithms import *
from utils import *
import matplotlib.pyplot as plt
from time import perf_counter_ns

def operation_count_plot():
    # Lists to store data for plotting
    exhaustive_nodes = []
    exhaustive_ops = []
    
    greedy_nodes = []
    greedy_ops = []

    # Test exhaustive algorithm
    for n in range(2, 1000, 1):
        m_prob = 0.5
        random_graph = generate_graph(n, m_prob)
        print(f"Testing exhaustive with {n} nodes")
        _, _, ops = exhaustive_min_cut(random_graph)
        
        exhaustive_nodes.append(n)
        exhaustive_ops.append(ops)
        
        if ops > 1000000:  # arbitrary limit to stop exponential growth
            break

    # Test greedy algorithm
    for n in range(2, 1000, 1):
        m_prob = 0.5
        random_graph = generate_graph(n, m_prob)
        print(f"Testing greedy with {n} nodes")
        _, _, ops = greedy_min_cut(random_graph)
        
        greedy_nodes.append(n)
        greedy_ops.append(ops)
        
        if ops > 1000000:  # same limit for comparison
            break

    # Regular scale plot
    plt.figure(figsize=(10, 6))
    plt.plot(exhaustive_nodes, exhaustive_ops, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_ops, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations')
    plt.title('Operations vs Number of Nodes')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('operations_comparison_regular.png')
    plt.close()
    
    # Log scale plot
    plt.figure(figsize=(10, 6))
    plt.plot(exhaustive_nodes, exhaustive_ops, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_ops, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations (log scale)')
    plt.title('Operations vs Number of Nodes (Log Scale)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('operations_comparison_log.png')
    plt.close()

    # Print some key points for analysis
    print("\nKey Points:")
    print(f"Exhaustive algorithm reached {exhaustive_ops[-1]} operations with {exhaustive_nodes[-1]} nodes")
    print(f"Greedy algorithm reached {greedy_ops[-1]} operations with {greedy_nodes[-1]} nodes")
    
def execution_time_plot():
        # Lists to store data for plotting
    exhaustive_nodes = []
    exhaustive_times = []
    
    greedy_nodes = []
    greedy_times = []

    # Test exhaustive algorithm
    for n in range(2, 100, 1):
        m_prob = 0.75
        random_graph = generate_graph_erdos_renyi(n, m_prob)
        print(f"Testing exhaustive with {n} nodes", end='; ')
        if n == 13:
            visualize_and_save_graph(random_graph, f"graph_{n}_nodes.png")
        
        start = perf_counter_ns()
        _, min_cut_partition, _ = exhaustive_min_cut(random_graph)
        if n == 13:
            visualize_min_cut(random_graph, min_cut_partition, "exhaustive_min_cut.png")
        end = perf_counter_ns()
        time_taken = (end - start) * 1e-9  # Convert to seconds
        
        exhaustive_nodes.append(n)
        exhaustive_times.append(time_taken)
        
        print(f"Time taken: {time_taken:.2f} seconds")
        if time_taken > 300:  # Stop if execution takes more than 5 seconds
            break

    # Test greedy algorithm
    #for n in range(2, 10000, 1):
    #    m_prob = 0.75
    #    random_graph = generate_graph_erdos_renyi(n, m_prob)
    #    print(f"Testing greedy with {n} nodes", end='; ')
    #    
    #    start = perf_counter_ns()
    #    greedy_min_cut(random_graph)
    #    end = perf_counter_ns()
    #    time_taken = (end - start) * 1e-9  # Convert to seconds
    #    
    #    greedy_nodes.append(n)
    #    greedy_times.append(time_taken)
    #    
    #    print(f"Time taken: {time_taken:.2f} seconds")
    #    if time_taken > 15:  # Stop if execution takes more than 1 seconds
    #        break

    # Regular scale plot
    plt.figure(figsize=(10, 6))
    plt.plot(exhaustive_nodes, exhaustive_times, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_times, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Number of Nodes')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('time_comparison_regular.png')
    plt.close()
    
    # Log scale plot
    plt.figure(figsize=(10, 6))
    plt.plot(exhaustive_nodes, exhaustive_times, 'r-', label='Exhaustive')
    plt.plot(greedy_nodes, greedy_times, 'b-', label='Greedy')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds, log scale)')
    plt.title('Execution Time vs Number of Nodes (Log Scale)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('time_comparison_log.png')
    plt.close()

    # Print some key points for analysis
    print("\nKey Points:")
    print(f"Exhaustive algorithm reached {exhaustive_times[-1]:.2f} seconds with {exhaustive_nodes[-1]} nodes")
    print(f"Greedy algorithm reached {greedy_times[-1]:.2f} seconds with {greedy_nodes[-1]} nodes")
    
def create_trap_graph():
    G = nx.Graph()
    
    # Add 10 nodes
    G.add_nodes_from(range(10))
    
    # Create a dense first component (almost complete)
    for i in range(4):
        for j in range(i+1, 4):
            G.add_edge(i, j)
    
    # Create a dense second component (almost complete)
    for i in range(4, 8):
        for j in range(i+1, 8):
            G.add_edge(i, j)
            
    # Add bridge nodes with specific connections
    G.add_edge(3, 8)  # Connect first component to bridge
    G.add_edge(8, 9)  # Bridge connection
    G.add_edge(9, 4)  # Connect bridge to second component
    
    # Add extra edges to make balanced cut appealing to greedy
    G.add_edge(3, 9)
    G.add_edge(8, 4)
    G.add_edge(0, 4)
    G.add_edge(3, 7)
    
    return G

def compare_algorithms():
    # Create the trap graph
    G = create_trap_graph()
    
    # Visualize the original graph
    print("\nOriginal Graph:")
    visualize_and_save_graph(G, "trap_graph.png")
    
    # Run exhaustive algorithm
    print("\nExhaustive Search Results:")
    min_cut_weight, min_cut_partition, operations = exhaustive_min_cut(G)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {operations}")
    visualize_min_cut(G, min_cut_partition, "exhaustive_solution.png")
    
    # Run greedy algorithm
    print("\nGreedy Algorithm Results:")
    min_cut_weight, min_cut_partition, operations = greedy_min_cut(G)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    print(f"Operations: {operations}")
    visualize_min_cut(G, min_cut_partition, "greedy_solution.png")

if __name__ == "__main__":
    #execution_time_plot()
    
    #operation_count_plot()
    
    #compare_algorithms()
    
    pass