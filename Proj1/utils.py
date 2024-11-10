import random
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Use Agg backend instead of TkAgg
import matplotlib.pyplot as plt

# Genreate a graph with n nodes and m edges with random weights
def generate_random_graph(n, m):
    G = nx.Graph()
    nodes = list(range(n))
    
    # Add n nodes
    G.add_nodes_from(nodes)
    
    # Add m random edges with random weights, but avoid adding edges between the same node
    for _ in range(m):
        u, v = random.sample(nodes, 2)
        weight = random.randint(1, 10)
        G.add_edge(u, v, weight=weight)
    
    return G

# Print a graph be exporting it to a file using matplotlib
def print_graph(G, filename):
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(8, 6))
    
    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=500)
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos)
    
    # Draw the edge labels
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.axis('off')
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':        
    # Generate a random graph
    G = generate_random_graph(10, 20)
    print_graph(G, 'random_graph.png')