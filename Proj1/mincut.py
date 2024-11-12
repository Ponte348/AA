from utils import *
from algorithms import *

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
    min_cut_weight, min_cut_partition = exhaustive_min_cut(graph)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    
    visualize_min_cut(graph, min_cut_partition, "exhaustive_min_cut.png")

def test_greedy_min_cut(n, m_prob, graph):
    min_cut_weight, min_cut_partition = greedy_min_cut(graph)
    print(f"Minimum cut weight: {min_cut_weight}")
    print(f"Partition: {min_cut_partition}")
    
    visualize_min_cut(graph, min_cut_partition, "greedy_min_cut.png")

def main():
    n = 10  # number of nodes
    m_prob = 0.75 # probability of edge creation
    random_graph = generate_graph_powerlaw_cluster(n, 3, 0.5)
    
    # Visualize the graph
    #visualize_and_save_graph(random_graph, "random_graph.png")
    
    # Test the algorithms
    test_exhaustive_min_cut(n, m_prob, random_graph)
    
    test_greedy_min_cut(n, m_prob, random_graph)

if __name__ == "__main__":
    main()