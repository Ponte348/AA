import random
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Use Agg backend instead of TkAgg
import matplotlib.pyplot as plt

def generate_random_graph(n, m):
    """Generate a graph with n nodes and m edges with random weights"""
    G = nx.Graph()
    nodes = list(range(n))
    
    # Add n nodes
    G.add_nodes_from(nodes)
    
    # Add m random edges with random weights
    for _ in range(m):
        u, v = random.sample(nodes, 2)
        weight = random.randint(1, 10)
        G.add_edge(u, v, weight=weight)
    
    return G

def visualize_cut(G, partition, cut_value):
    """Visualize the graph with the minimum cut"""
    plt.figure(figsize=(15, 10))
    
    # Use a different layout for large graphs
    if len(G) > 100:
        pos = nx.kamada_kawai_layout(G)
    else:
        pos = nx.spring_layout(G)
    
    # Draw nodes with smaller size for large graphs
    node_size = 500 if len(G) < 50 else 50
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, nodelist=partition[0], node_color='lightblue', 
                          node_size=node_size, label='Set A')
    nx.draw_networkx_nodes(G, pos, nodelist=partition[1], node_color='lightgreen', 
                          node_size=node_size, label='Set B')
    
    # Draw edges
    cut_edges = [(u, v) for u in partition[0] for v in partition[1] if G.has_edge(u, v)]
    normal_edges = [e for e in G.edges() if e not in cut_edges and (e[1], e[0]) not in cut_edges]
    
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color='gray', alpha=0.2)
    nx.draw_networkx_edges(G, pos, edgelist=cut_edges, edge_color='red', width=2)
    
    # Add labels only for small graphs
    if len(G) < 50:
        nx.draw_networkx_labels(G, pos)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    plt.title(f"Minimum Cut = {cut_value}\nSet A size: {len(partition[0])}, Set B size: {len(partition[1])}")
    plt.legend()
    plt.axis('off')
    plt.savefig('mincut_graph.png', dpi=300, bbox_inches='tight')
    plt.close()
    
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

def print_cut_info(cut_value, partition, G):
    """Print information about the cut"""
    print(f"Minimum cut value: {cut_value}")
    print(f"Set A size: {len(partition[0])}")
    print(f"Set B size: {len(partition[1])}")
    
    # Print the actual cut edges
    cut_edges = [(u, v) for u in partition[0] for v in partition[1] if G.has_edge(u, v)]
    print("\nCut edges:")
    for u, v in cut_edges:
        weight = G[u][v]['weight']
        print(f"Edge {u}-{v} with weight {weight}")
    
    # Optional: print actual sets only if they're small
    if len(G) < 100:
        print(f"\nSet A: {partition[0]}")
        print(f"Set B: {partition[1]}")







if __name__ == '__main__':        
    # Generate a random graph
    G = generate_random_graph(10, 20)
    print_graph(G, 'random_graph.png')
    