import random
import time
from collections import defaultdict

def randomized_exhaustive_min_cut(G, max_time=60, max_iterations=1000):
    operations = 0
    n = G.number_of_nodes()
    min_cut = float('inf')
    best_partition = None
    
    # Keep track of tested partitions
    tested_partitions = set()
    start_time = time.time()
    
    # Dictionary to track success of different partition sizes
    size_success = defaultdict(lambda: {'attempts': 0, 'improvements': 0})
    
    for iteration in range(max_iterations):
        # Check time limit
        if time.time() - start_time >= max_time:
            break
            
        operations += 1
        
        # Generate random partition
        partition_size = random.randint(1, n-1)  # Random size for set_a
        set_a = set(random.sample(range(n), partition_size))
        partition_tuple = tuple(sorted(set_a))  # Make it hashable
        
        # Skip if already tested
        if partition_tuple in tested_partitions:
            continue
            
        tested_partitions.add(partition_tuple)
        
        set_b = set(range(n)) - set_a
        set_a = list(set_a)
        set_b = list(set_b)
        
        cut_size = 0
        for v1 in set_a:
            for v2 in set_b:
                operations += 1
                if G.has_edge(v1, v2):
                    cut_size += 1
        
        # Track success rate for this partition size
        size_success[partition_size]['attempts'] += 1
        if cut_size < min_cut:
            size_success[partition_size]['improvements'] += 1
            min_cut = cut_size
            best_partition = (set_a, set_b)
            
        # Every 100 iterations, adjust strategy based on success rates
        if iteration % 100 == 0:
            best_sizes = sorted(
                size_success.items(),
                key=lambda x: x[1]['improvements'] / max(x[1]['attempts'], 1),
                reverse=True
            )[:3]
            
            # Focus on most promising partition sizes
            if random.random() < 0.7 and best_sizes:  # 70% chance to use successful sizes
                partition_size = random.choice([size for size, _ in best_sizes])
    
    return min_cut, best_partition, operations, iteration + 1

def randomized_greedy_min_cut(G, max_time=60, max_iterations=1000, max_attempts_per_start=10):
    operations = 0
    n = G.number_of_nodes()
    global_min_cut = float('inf')
    global_best_partition = None
    start_time = time.time()
    tested_starts = set()
    
    for iteration in range(max_iterations):
        # Check time limit
        if time.time() - start_time >= max_time:
            break
            
        # Generate random initial partition
        partition_size = random.randint(n//3, 2*n//3)  # Keep it somewhat balanced
        initial_set_a = set(random.sample(range(n), partition_size))
        start_config = tuple(sorted(initial_set_a))
        
        # Skip if we've tried this starting point too many times
        if tested_starts.count(start_config) >= max_attempts_per_start:
            continue
            
        tested_starts.add(start_config)
        
        set_a = list(initial_set_a)
        set_b = list(set(range(n)) - initial_set_a)
        
        best_cut_size = 0
        for v1 in set_a:
            for v2 in set_b:
                operations += 1
                if G.has_edge(v1, v2):
                    best_cut_size += 1
                    
        best_partition = (set_a.copy(), set_b.copy())
        
        # Random number of improvement attempts
        improvement_attempts = random.randint(n//2, n*2)
        
        for attempt in range(improvement_attempts):
            operations += 1
            current_best_gain = 0
            candidates = []
            
            # Randomly sample vertices to consider moving
            vertices_to_check = random.sample(range(n), min(n, n//2))
            
            for v in vertices_to_check:
                operations += 1
                
                if v in set_a and len(set_a) > 1:
                    source, dest = set_a, set_b
                elif v in set_b and len(set_b) > 1:
                    source, dest = set_b, set_a
                else:
                    continue
                    
                old_edges = sum(1 for u in dest if G.has_edge(v, u))
                new_edges = sum(1 for u in source if G.has_edge(v, u))
                gain = old_edges - new_edges
                
                if gain >= current_best_gain:
                    candidates.append((gain, v, source))
                    current_best_gain = gain
            
            # If no improvement possible, possibly continue with small probability
            if not candidates or current_best_gain <= 0:
                if random.random() >= 0.1:  # 90% chance to break
                    break
                continue
            
            # Randomly select from top candidates
            top_candidates = [c for c in candidates if c[0] == current_best_gain]
            gain, best_vertex, best_source = random.choice(top_candidates)
            
            # Make the move
            if best_source == set_a:
                set_a.remove(best_vertex)
                set_b.append(best_vertex)
            else:
                set_b.remove(best_vertex)
                set_a.append(best_vertex)
                
            current_cut_size = 0
            for v1 in set_a:
                for v2 in set_b:
                    operations += 1
                    if G.has_edge(v1, v2):
                        current_cut_size += 1
                        
            if current_cut_size < best_cut_size:
                best_cut_size = current_cut_size
                best_partition = (set_a.copy(), set_b.copy())
        
        if best_cut_size < global_min_cut:
            global_min_cut = best_cut_size
            global_best_partition = best_partition
    
    return global_min_cut, global_best_partition, operations, iteration + 1