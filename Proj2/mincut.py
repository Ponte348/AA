import networkx as nx
import random
from typing import Tuple, Set, List
from utils import visualize_min_cut

def karger_min_cut(G: nx.Graph) -> Tuple[int, Tuple[Set, Set]]:
    def contract(G: nx.Graph, u: int, v: int, vertex_groups: dict) -> None:
        """Contract edge (u,v) in graph G, updating vertex groups."""
        # Add v's edges to u (except self loops)
        for w in G.neighbors(v):
            if w != u:  # Avoid self loops
                G.add_edge(u, w)
        
        # Merge vertex groups
        vertex_groups[u].update(vertex_groups[v])
        del vertex_groups[v]
        
        # Remove contracted vertex
        G.remove_node(v)

    def single_cut(G: nx.Graph) -> Tuple[int, Tuple[Set, Set]]:
        """Perform one iteration of Karger's algorithm."""
        # Work on a copy of the graph
        G_working = G.copy()
        
        # Initialize vertex groups - each vertex starts in its own group
        vertex_groups = {v: {v} for v in G_working.nodes()}
        
        # Contract edges until only 2 vertices remain
        while G_working.number_of_nodes() > 2:
            if not G_working.edges():  # Handle disconnected graphs
                break
                
            # Select a random edge
            u, v = random.choice(list(G_working.edges()))
            
            # Contract the edge
            contract(G_working, u, v, vertex_groups)
        
        # Get the two partitions
        partitions = list(vertex_groups.values())
        
        # If we don't have exactly two partitions, the graph was disconnected
        if len(partitions) != 2:
            return float('inf'), (set(), set())
        
        # Count edges between partitions in original graph
        cut_size = sum(1 for u in partitions[0] 
                      for v in partitions[1] 
                      if G.has_edge(u, v))
        
        return cut_size, (partitions[0], partitions[1])

    # Number of iterations to run
    iterations = G.number_of_nodes() * 2
    
    # Track best cut
    best_cut = float('inf')
    best_partition = None
    
    # Run algorithm multiple times
    for _ in range(iterations):
        cut_size, partition = single_cut(G)
        if cut_size < best_cut:
            best_cut = cut_size
            best_partition = partition
    
    # If no valid cut was found, return trivial cut
    if best_partition is None:
        nodes = list(G.nodes())
        return len(G.edges()), ({nodes[0]}, set(nodes[1:]))
        
    return best_cut, best_partition

# Function to create and save the graph
def create_and_save_graph(n_nodes: int, edge_prob: float) -> nx.Graph:
    from utils import generate_graph_erdos_renyi, visualize_and_save_graph, visualize_min_cut
    
    # Generate the graph
    G = generate_graph_erdos_renyi(n_nodes, edge_prob)
    
    # Save the original graph
    visualize_and_save_graph(G, f"graph_{n_nodes}_nodes.png")
    
    return G

# Example usage
def main():
    n_nodes = 15
    edge_prob = 0.5

    G = create_and_save_graph(n_nodes, edge_prob)
    
    # Find min cut using both algorithms
    # For the Stoer-Wagner algorithm we can use NetworkX's built-in function
    print("Finding minimum cut using Stoer-Wagner algorithm...")
    sw_cut_size, sw_partition = nx.stoer_wagner(G)
    print(f"Stoer-Wagner min cut size: {sw_cut_size}")
    
    print("\nFinding minimum cut using Karger's algorithm...")
    karger_cut_size, karger_partition = karger_min_cut(G)
    print(f"Karger min cut size: {karger_cut_size}")
    
    # Visualize the cuts
    visualize_min_cut(G, sw_partition, f"min_cut_stoer_wagner_{n_nodes}_nodes.png")
    visualize_min_cut(G, karger_partition, f"min_cut_karger_{n_nodes}_nodes.png")

if __name__ == "__main__":
    main()