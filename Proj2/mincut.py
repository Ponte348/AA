import networkx as nx
import random
from typing import Tuple, Set, List
from utils import generate_graph_erdos_renyi, visualize_and_save_graph, visualize_min_cut
from time import perf_counter_ns
import matplotlib.pyplot as plt

def karger_min_cut(G: nx.Graph) -> Tuple[int, Tuple[Set, Set]]:
    operations = 0 # to count num of operations
    
    """ From wikipedia:
    procedure contract(G=(V,E)):
    while |V| > 2:
        choose e ∈ E uniformly at random
        G = G / e
    return the only cut in G
    """
    def contract(G: nx.Graph, u: int, v: int, vertex_groups: dict):
        """Contract edge (u,v) in graph G, updating vertex groups."""
        nonlocal operations # so we can update the operations count
        
        # add v's edges to u (except self loops)
        for w in G.neighbors(v):
            operations += 1
            if w != u:
                G.add_edge(u, w)
        
        # merge vertex groups
        vertex_groups[u].update(vertex_groups[v])
        del vertex_groups[v]
        
        # remove contracted vertex
        G.remove_node(v)

    def single_cut(G: nx.Graph) -> Tuple[int, Tuple[Set, Set]]:
        """Perform one iteration of Karger's algorithm."""
        nonlocal operations
        
        G_working = G.copy()
        
        # initialize vertex groups - each vertex starts in its own group
        vertex_groups = {v: {v} for v in G_working.nodes()}
        
        # contract edges until only 2 vertices remain
        while G_working.number_of_nodes() > 2:
            operations += 1
            if not G_working.edges():  # disconnected graph
                break
                
            # select a random edge
            u, v = random.choice(list(G_working.edges()))
            
            # contract the edge
            contract(G_working, u, v, vertex_groups)
        
        # get the two partitions
        partitions = list(vertex_groups.values())
        
        # if we don't have exactly two partitions, the graph was disconnected
        if len(partitions) != 2:
            return float('inf'), (set(), set())
        
        # count edges between partitions in original graph
        cut_size = 0
        for u in partitions[0]:
            for v in partitions[1]:
                operations += 1
                if G.has_edge(u, v):
                    cut_size += 1
        
        return cut_size, (partitions[0], partitions[1])

    # number of iterations to run
    iterations = G.number_of_nodes() * 2
    
    # keep track best cut
    best_cut = float('inf')
    best_partition = None
    
    # run algorithm multiple times
    for _ in range(iterations): # O(n^2) iterations
        operations += 1
        cut_size, partition = single_cut(G) # O(n^2) per iteration
        if cut_size < best_cut:
            best_cut = cut_size
            best_partition = partition
    
    # if no valid cut was found, return the original graph
    if best_partition is None:
        nodes = list(G.nodes())
        return len(G.edges()), ({nodes[0]}, set(nodes[1:]))
        
    return best_cut, best_partition, operations

# create the graph for our problem and save it for visualization
def create_and_save_graph(n_nodes: int, edge_prob: float) -> nx.Graph:
    
    G = generate_graph_erdos_renyi(n_nodes, edge_prob)
    
    visualize_and_save_graph(G, f"graph_{n_nodes}_nodes.png")
    
    return G

def karger_analysis_plots(max_nodes=50):
    # lists to store data for plotting
    nodes_list = []
    operations_list = []
    times_list = []
    # the graphs of these sizes will be saved for visualization
    min_cut_visualizations = [8, 16, 24, 48, 60, 80, 100, 125, 150, 200, 250]

    # test Karger's algorithm
    for n in range(2, max_nodes, 1):
        m_prob = 0.5
        G = generate_graph_erdos_renyi(n, m_prob)
        print(f"Testing Karger with {n} nodes", end='; ')
        
        # time measurement
        start = perf_counter_ns()
        karger_cut_size, karger_partition, operations = karger_min_cut(G)
        end = perf_counter_ns()
        time_taken = (end - start) * 1e-9  # convert to seconds
        
        if n in min_cut_visualizations:
            visualize_min_cut(G, karger_partition, f"min_cut_karger_{n}_nodes.png")
        
        nodes_list.append(n)
        operations_list.append(operations)
        times_list.append(time_taken)
        
        print(f"Time taken: {time_taken:.2f} seconds, Operations: {operations}")
        
        # stop if execution takes more than 5 minutes
        if time_taken > 300:
            break

    # Operations plot (regular scale)
    plt.figure(figsize=(10, 6))
    plt.plot(nodes_list, operations_list, 'g-', label='Karger')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations')
    plt.title('Operations vs Number of Nodes (Karger\'s Algorithm)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('karger_operations_regular.png')
    plt.close()
    
    # Operations plot (log scale)
    plt.figure(figsize=(10, 6))
    plt.plot(nodes_list, operations_list, 'g-', label='Karger')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations (log scale)')
    plt.title('Operations vs Number of Nodes (Karger\'s Algorithm) - Log Scale')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('karger_operations_log.png')
    plt.close()

    # Time plot (regular scale)
    plt.figure(figsize=(10, 6))
    plt.plot(nodes_list, times_list, 'g-', label='Karger')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Number of Nodes (Karger\'s Algorithm)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('karger_time_regular.png')
    plt.close()
    
    # Time plot (log scale)
    plt.figure(figsize=(10, 6))
    plt.plot(nodes_list, times_list, 'g-', label='Karger')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds, log scale)')
    plt.title('Execution Time vs Number of Nodes (Karger\'s Algorithm) - Log Scale')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('karger_time_log.png')
    plt.close()

    # Print some key points for analysis
    print("\nKey Points:")
    print(f"Final number of nodes tested: {nodes_list[-1]}")
    print(f"Final operation count: {operations_list[-1]}")
    print(f"Final execution time: {times_list[-1]:.2f} seconds")

# example
def main():
    #n_nodes = 30
    #edge_prob = 0.5

    #G = create_and_save_graph(n_nodes, edge_prob)
    #
    ## Find min cut using both algorithms
    #
    ## we can use the stoer wagner's built-in for a comparison
    #print("Finding minimum cut using Stoer-Wagner algorithm...")
    #sw_cut_size, sw_partition = nx.stoer_wagner(G)
    #print(f"Stoer-Wagner min cut size: {sw_cut_size}")
    #
    ## now we use our algorithm
    #print("\nFinding minimum cut using Karger's algorithm...")
    #karger_cut_size, karger_partition, operations = karger_min_cut(G)
    #print(f"Karger min cut size: {karger_cut_size}")
    #
    ## Visualize the cuts
    #visualize_min_cut(G, sw_partition, f"min_cut_stoer_wagner_{n_nodes}_nodes.png")
    #visualize_min_cut(G, karger_partition, f"min_cut_karger_{n_nodes}_nodes.png")

    karger_analysis_plots(max_nodes=250)

if __name__ == "__main__":
    main()