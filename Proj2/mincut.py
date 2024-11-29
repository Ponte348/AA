import networkx as nx
import random
from typing import Tuple, Set, List
from utils import generate_graph_erdos_renyi, visualize_and_save_graph, visualize_min_cut

def karger_min_cut(G: nx.Graph) -> Tuple[int, Tuple[Set, Set]]:
    """ From wikipedia:
    procedure contract(G=(V,E)):
    while |V| > 2:
        choose e ∈ E uniformly at random
        G = G / e
    return the only cut in G
    """
    def contract(G: nx.Graph, u: int, v: int, vertex_groups: dict):
        """Contract edge (u,v) in graph G, updating vertex groups."""
        # add v's edges to u (except self loops)
        for w in G.neighbors(v):
            if w != u:
                G.add_edge(u, w)
        
        # merge vertex groups
        vertex_groups[u].update(vertex_groups[v])
        del vertex_groups[v]
        
        # remove contracted vertex
        G.remove_node(v)

    def single_cut(G: nx.Graph) -> Tuple[int, Tuple[Set, Set]]:
        """Perform one iteration of Karger's algorithm."""
        G_working = G.copy()
        
        # initialize vertex groups - each vertex starts in its own group
        vertex_groups = {v: {v} for v in G_working.nodes()}
        
        # contract edges until only 2 vertices remain
        while G_working.number_of_nodes() > 2:
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
        cut_size = sum(1 for u in partitions[0] for v in partitions[1] if G.has_edge(u, v))
        
        return cut_size, (partitions[0], partitions[1])

    # number of iterations to run
    iterations = G.number_of_nodes() * 2
    
    # keep track best cut
    best_cut = float('inf')
    best_partition = None
    
    # run algorithm multiple times
    for _ in range(iterations): # O(n^2) iterations
        cut_size, partition = single_cut(G) # O(n^2) per iteration
        if cut_size < best_cut:
            best_cut = cut_size
            best_partition = partition
    
    # if no valid cut was found, return the original graph
    if best_partition is None:
        nodes = list(G.nodes())
        return len(G.edges()), ({nodes[0]}, set(nodes[1:]))
        
    return best_cut, best_partition

# Function to create and save the graph
def create_and_save_graph(n_nodes: int, edge_prob: float) -> nx.Graph:
    
    # Generate the graph
    G = generate_graph_erdos_renyi(n_nodes, edge_prob)
    
    # Save the original graph
    visualize_and_save_graph(G, f"graph_{n_nodes}_nodes.png")
    
    return G

# Example usage
def main():
    n_nodes = 30
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