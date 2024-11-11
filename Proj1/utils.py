import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(nodes, edge_prob):
    # k is the number of nearest neighbors each node is connected to
    # k must be even and less than nodes
    k = min(nodes-1, max(2, int(edge_prob * nodes)))
    if k % 2 == 1:
        k -= 1

    # probability of rewiring each edge
    p = edge_prob
    # seed is NMec multiplied by a random prime number
    seed = 98059  
    graph = nx.connected_watts_strogatz_graph(nodes, k, p, seed)
    return graph


def generate_graph_random_regular(nodes, degree):
    """
    Creates a random regular graph where each node has exactly the same degree.
    degree must be less than nodes and nodes * degree must be even
    """
    if degree >= nodes:
        degree = nodes - 1
    if (nodes * degree) % 2 == 1:
        degree -= 1
    graph = nx.random_regular_graph(degree, nodes, seed=98059)
    return graph

def generate_graph_powerlaw_cluster(nodes, m, p):
    """
    Creates a graph using the Holme and Kim algorithm for growing graphs with powerlaw
    degree distribution and approximate average clustering.
    m: number of random edges to add for each new node
    p: probability of adding a triangle after adding a random edge
    """
    if m >= nodes:
        m = nodes - 1
    seed = 98059
    graph = nx.powerlaw_cluster_graph(nodes, m, p, seed)
    return graph

def visualize_and_save_graph(G, filename="graph.png"):
    plt.figure(figsize=(10,10))
    
    # Get position of nodes
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def main():
    # Example usage
    n = 15  # number of nodes
    #m = 45  # number of edges
    m_prob = 0.4 # probability of edge creation
    random_graph = generate_graph(n, m_prob)
    visualize_and_save_graph(random_graph, "random_graph.png")
    
if __name__ == "__main__":
    main()