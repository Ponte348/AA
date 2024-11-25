def exhaustive_min_cut(G):
    operations = 0
    n = G.number_of_nodes()
    min_cut = float('inf')
    best_partition = None

    for i in range(1, 2**(n-1)): # O(2^n)
        operations += 1 # Partition generation
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
        for v in range(n): # O(n) - doesn't count towards complexity, so we don't count it in operations
            if partition[v] == '0':
                set_a.append(v)
            else:
                set_b.append(v)
                
        for v1 in set_a: # O(n^2)
            for v2 in set_b:
                operations += 1 # Edge check
                if G.has_edge(v1, v2):
                    cut_size += 1
        
        if cut_size < min_cut:
            min_cut = cut_size
            best_partition = (set_a, set_b)
    
    return min_cut, best_partition, operations

def greedy_min_cut(G):
    operations = 0
    n = G.number_of_nodes()
    
    # Start with roughly balanced partitions
    mid = n // 2
    set_a = list(range(mid))
    set_b = list(range(mid, n))
    
    best_cut_size = 0
    for v1 in set_a:
        for v2 in set_b:
            operations += 1  # edge check
            if G.has_edge(v1, v2):
                best_cut_size += 1
                
    best_partition = (set_a.copy(), set_b.copy())
    
    # Maximum number of iterations = number of nodes
    # since we can't improve more times than we have nodes
    for _ in range(n): # O(n)
        operations += 1 # Iteration
        current_best_gain = 0
        best_vertex = None
        best_source = None
        
        # Try moving each vertex from one set to another
        for v in range(n): # O(n)
            operations += 1 # Vertex check
            
            if v in set_a and len(set_a) > 1:
                source, dest = set_a, set_b
            elif v in set_b and len(set_b) > 1:
                source, dest = set_b, set_a
            else:
                continue
                
            # Calculate gain of moving vertex v - doesn't count towards complexity
            old_edges = sum(1 for u in dest if G.has_edge(v, u)) # O(n)
            new_edges = sum(1 for u in source if G.has_edge(v, u)) # O(n)
            gain = old_edges - new_edges
            
            if gain > current_best_gain:
                current_best_gain = gain
                best_vertex = v
                best_source = source
        
        # If no improvement possible, break
        if current_best_gain <= 0:
            break
            
        # Make the best move
        if best_source == set_a:
            set_a.remove(best_vertex)
            set_b.append(best_vertex)
        else:
            set_b.remove(best_vertex)
            set_a.append(best_vertex)
            
        current_cut_size = 0
        for v1 in set_a:
            for v2 in set_b:
                operations += 1  # edge check O(n^2)
                if G.has_edge(v1, v2):
                    current_cut_size += 1
                    
        if current_cut_size < best_cut_size:
            best_cut_size = current_cut_size
            best_partition = (set_a.copy(), set_b.copy())
    
    return best_cut_size, best_partition, operations