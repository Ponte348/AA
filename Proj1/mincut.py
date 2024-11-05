import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Use Agg backend instead of TkAgg
import matplotlib.pyplot as plt

def find_minimum_cut(G):
    """
    Find the minimum cut in an undirected graph using NetworkX.
    Returns the cut value and the two sets of nodes.
    """
    if not nx.is_connected(G):
        return 0, [], []  # If graph is not connected, min cut is 0
    
    # Convert G to an undirected graph if it isn't already
    if not G.is_directed():
        G = G.copy()
    
    # Get the cut value and partition using stoer_wagner algorithm
    cut_value, partition = nx.stoer_wagner(G)
    set_a, set_b = partition
    
    return cut_value, list(set_a), list(set_b)

def main():
    # Create a sample graph
    G = nx.Graph()
    
    # Add edges with weights
    edges = [
        (0, 1, 2),  # (node1, node2, weight)
        (0, 2, 3),
        (1, 3, 2),
        (2, 3, 1)
    ]
    
    G.add_weighted_edges_from(edges)
    
    # Find minimum cut
    cut_value, set_a, set_b = find_minimum_cut(G)
    
    print(f"Minimum cut value: {cut_value}")
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # Visualize the graph and the cut
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(8, 6))
    
    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, nodelist=set_a, node_color='lightblue', 
                          node_size=500, label='Set A')
    nx.draw_networkx_nodes(G, pos, nodelist=set_b, node_color='lightgreen', 
                          node_size=500, label='Set B')
    
    # Draw edges
    cut_edges = [(u, v) for u in set_a for v in set_b if G.has_edge(u, v)]
    normal_edges = [(u, v) for (u, v) in G.edges() if (u, v) not in cut_edges and (v, u) not in cut_edges]
    
    # Draw normal edges
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color='gray')
    # Draw cut edges in red
    nx.draw_networkx_edges(G, pos, edgelist=cut_edges, edge_color='red', width=2)
    
    # Add labels
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    plt.title(f"Minimum Cut = {cut_value}")
    plt.legend()
    plt.axis('off')
    
    # Save the plot instead of showing it
    plt.savefig('mincut_graph.png')
    print("\nGraph visualization has been saved as 'mincut_graph.png'")
    plt.close()

if __name__ == "__main__":
    main()