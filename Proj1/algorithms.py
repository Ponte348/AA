def exhaustive_min_cut(G):
    n = G.number_of_nodes()
    min_cut = float('inf')
    best_partition = None

    for i in range(1, 2**(n-1)):
        # Convert number to binary to represent partitions
        partition = bin(i)[2:].zfill(n)
        
        """Example: For a graph with 5 nodes,
        00001 represents set_a = {0, 1, 2, 3} and set_b = {4}
        10011 represents set_a = {1, 2} and set_b = {0, 3, 4}
        """
        
        cut_size = 0
        set_a = []
        set_b = []
        
        # Split vertices into sets
        for v in range(n):
            if partition[v] == '0':
                set_a.append(v)
            else:
                set_b.append(v)
                
        for v1 in set_a:
            for v2 in set_b:
                if G.has_edge(v1, v2):
                    cut_size += 1
        
        if cut_size < min_cut:
            min_cut = cut_size
            best_partition = (set_a, set_b)
    
    return min_cut, best_partition

def greedy_min_cut(G):
    n = G.number_of_nodes()
    
    # Start with roughly balanced partitions
    mid = n // 2
    set_a = list(range(mid))
    set_b = list(range(mid, n))
    best_cut_size = sum(1 for v1 in set_a for v2 in set_b if G.has_edge(v1, v2))
    best_partition = (set_a.copy(), set_b.copy())
    
    improved = True
    while improved:
        improved = False
        current_best_gain = 0
        best_vertex = None
        best_source = None
        
        # Try moving each vertex from one set to another
        for v in range(n):
            if v in set_a and len(set_a) > 1:  # Ensure set_a doesn't become empty
                source, dest = set_a, set_b
            elif v in set_b and len(set_b) > 1:  # Ensure set_b doesn't become empty
                source, dest = set_b, set_a
            else:
                continue
                
            # Calculate gain of moving vertex v
            old_edges = sum(1 for u in dest if G.has_edge(v, u))
            new_edges = sum(1 for u in source if G.has_edge(v, u))
            gain = old_edges - new_edges
            
            if gain > current_best_gain:
                current_best_gain = gain
                best_vertex = v
                best_source = source
        
        # Make the best move if it improves the cut
        if current_best_gain > 0:
            if best_source == set_a:
                set_a.remove(best_vertex)
                set_b.append(best_vertex)
            else:
                set_b.remove(best_vertex)
                set_a.append(best_vertex)
                
            current_cut_size = sum(1 for v1 in set_a for v2 in set_b if G.has_edge(v1, v2))
            if current_cut_size < best_cut_size:
                best_cut_size = current_cut_size
                best_partition = (set_a.copy(), set_b.copy())
            improved = True
    
    return best_cut_size, best_partition