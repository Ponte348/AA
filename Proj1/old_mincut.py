import random
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

from old_utils import *

def minimum_cut_phase(G, a):
    """Implementation of MINIMUMCUTPHASE from the paper"""
    A = {a}
    vertices_order = [a]
    weights = defaultdict(int)
    
    # Initialize weights for vertices connected to a
    for _, v, w in G.edges(a, data='weight', default=1):
        weights[v] = w
    
    remaining_vertices = set(G.nodes()) - A
    while remaining_vertices:
        # Find most tightly connected vertex
        max_weight = -float('inf')
        next_vertex = None
        
        for v in remaining_vertices:
            w = weights[v]
            if w > max_weight:
                max_weight = w
                next_vertex = v
        
        # Add vertex to A
        A.add(next_vertex)
        vertices_order.append(next_vertex)
        remaining_vertices.remove(next_vertex)
        
        # Update weights for remaining vertices
        for _, v, w in G.edges(next_vertex, data='weight', default=1):
            if v in remaining_vertices:
                weights[v] += w
    
    s, t = vertices_order[-2:]
    cut_weight = sum(w for _, v, w in G.edges(t, data='weight', default=1))
    
    return cut_weight, s, t, vertices_order

def merge_vertices(G, s, t):
    """Merge vertices s and t in graph G"""
    new_vertex = f"{s}-{t}"
    G.add_node(new_vertex)
    
    for v in G.neighbors(s):
        if v != t:
            w_sv = G.edges[s, v].get('weight', 1)
            w_tv = G.edges[t, v]['weight'] if G.has_edge(t, v) else 0
            G.add_edge(new_vertex, v, weight=w_sv + w_tv)
    
    for v in G.neighbors(t):
        if v != s and not G.has_edge(new_vertex, v):
            w_tv = G.edges[t, v].get('weight', 1)
            G.add_edge(new_vertex, v, weight=w_tv)
    
    G.remove_nodes_from([s, t])
    return new_vertex

def minimum_cut(G, starting_vertex=None):
    """Find the minimum cut in the graph"""
    if not starting_vertex:
        starting_vertex = list(G.nodes())[0]
    
    G = G.copy()
    min_cut_weight = float('inf')
    min_cut_partition = None
    original_nodes = {v: {v} for v in G.nodes()}  # Track original nodes
    
    while len(G) > 1:
        cut_weight, s, t, vertex_order = minimum_cut_phase(G, starting_vertex)
        
        if cut_weight < min_cut_weight:
            min_cut_weight = cut_weight
            
            # Reconstruct the partition using original nodes
            merged_nodes = set()
            for v in vertex_order[:-1]:  # All nodes except last
                merged_nodes.update(original_nodes[v])
            min_cut_partition = (list(merged_nodes), 
                               list(original_nodes[vertex_order[-1]]))
        
        # Merge vertices
        new_vertex = merge_vertices(G, s, t)
        # Update tracking of original nodes
        original_nodes[new_vertex] = original_nodes[s].union(original_nodes[t])
        del original_nodes[s]
        del original_nodes[t]
        
        if starting_vertex in (s, t):
            starting_vertex = new_vertex
    
    return min_cut_weight, min_cut_partition

def main():
    # Generate random graph
    n_vertices = 10  # Keep it small for better visualization
    m_edges = 20 # Max value: n_vertices * (n_vertices - 1) / 2
    
    # Generate a random graph
    G = generate_random_graph(n_vertices, m_edges)
    
    # Use NetworkX's implementation of Stoer-Wagner
    cut_value, partition = nx.stoer_wagner(G)
    
    # Print information about the cut
    print_cut_info(cut_value, partition, G)
    
    # Visualize the result
    visualize_cut(G, partition, cut_value)
    print("\nGraph visualization has been saved as 'mincut_graph.png'")
    
    
if __name__ == "__main__":
    main()