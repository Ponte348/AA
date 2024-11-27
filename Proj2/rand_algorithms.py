import random
import time
from collections import defaultdict

def randomized_exhaustive_min_cut(G, max_time=60, max_iterations=1000):
    operations = 0
    n = G.number_of_nodes()
    min_cut = float('inf')
    best_partition = None
    
    # keep track of tested partitions
    tested_partitions = set()
    start_time = time.time()
    
    # dictionary to check success of different partition sizes
    size_success = defaultdict(lambda: {'attempts': 0, 'improvements': 0})
    
    for iteration in range(max_iterations):

        if time.time() - start_time >= max_time:
            break
            
        operations += 1
        
        # random partition
        partition_size = random.randint(1, n-1)  # random size for set a
        set_a = set(random.sample(range(n), partition_size))
        partition_tuple = tuple(sorted(set_a))  # make it hashable
        
        # skip if already tested
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
        
        # keep track success rate for this partition size
        size_success[partition_size]['attempts'] += 1
        if cut_size < min_cut:
            size_success[partition_size]['improvements'] += 1
            min_cut = cut_size
            best_partition = (set_a, set_b)
            
        # every 100 iterations change strategy based on success rates
        if iteration % 100 == 0:
            best_sizes = sorted(
                size_success.items(),
                key=lambda x: x[1]['improvements'] / max(x[1]['attempts'], 1),
                reverse=True
            )[:3]
            
            # choose the most promising partition sizes
            if random.random() < 0.7 and best_sizes:  # 70% chance to use successful sizes
                partition_size = random.choice([size for size, _ in best_sizes])
    
    return min_cut, best_partition, operations, iteration + 1

def randomized_greedy_min_cut(G, max_time=60, max_iterations=1000, max_attempts_per_start=10):
    operations = 0
    n = G.number_of_nodes()
    global_min_cut = float('inf')
    global_best_partition = None
    start_time = time.time()

    # tested_starts to track attempts
    tested_starts = defaultdict(int)  # tracks the number of times each start_config is tested

    for iteration in range(max_iterations):

        if time.time() - start_time >= max_time:
            break

        # random initial partition
        partition_size = random.randint(n // 3, 2 * n // 3)  # Keep it somewhat balanced
        initial_set_a = set(random.sample(range(n), partition_size))
        start_config = tuple(sorted(initial_set_a))

        # skip if we've tried this starting point too many times
        if tested_starts[start_config] >= max_attempts_per_start:
            continue

        # increment start_config
        tested_starts[start_config] += 1

        set_a = list(initial_set_a)
        set_b = list(set(range(n)) - initial_set_a)

        # initial cut size
        best_cut_size = 0
        for v1 in set_a:
            for v2 in set_b:
                operations += 1
                if G.has_edge(v1, v2):
                    best_cut_size += 1

        best_partition = (set_a.copy(), set_b.copy())

        # rand num of improvement attempts
        improvement_attempts = random.randint(n // 2, n * 2)

        for attempt in range(improvement_attempts):
            operations += 1
            current_best_gain = 0
            candidates = []

            # Randomly sample vertices to consider moving
            vertices_to_check = random.sample(range(n), min(n, n // 2))

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

            # if no improvement possible, possibly continue with small probability
            if not candidates or current_best_gain <= 0:
                if random.random() >= 0.1:  # 90% chance to break
                    break
                continue

            # randomly select from top candidates
            top_candidates = [c for c in candidates if c[0] == current_best_gain]
            gain, best_vertex, best_source = random.choice(top_candidates)

            # make the move
            if best_source == set_a:
                set_a.remove(best_vertex)
                set_b.append(best_vertex)
            else:
                set_b.remove(best_vertex)
                set_a.append(best_vertex)

            # current cut size
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


"""
New algorithms
"""
def karger_min_cut(graph):
    """
    Calculates the minimum cut of a graph using Karger's Randomized Algorithm.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Example: {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    
    Returns:
        int: The minimum cut (number of crossing edges).
    """
    # if the graph has only two nodes, return the number of edges between them
    if len(graph) == 2:
        nodes = list(graph.keys())
        return len(graph[nodes[0]])  # num of edges between the two remaining nodes

    # Step 1: pick a random edge (u, v) to contract
    u = random.choice(list(graph.keys()))         # rand node u
    v = random.choice(graph[u])                   # rand neighbor v

    # Step 2: merge v into u and remove v from the graph
    # append all edges of v to u
    for neighbor in graph[v]:
        if neighbor != u:  # important to avoid self-loops
            graph[u].append(neighbor)
        graph[neighbor] = [u if x == v else x for x in graph[neighbor]]  # replace v with u in neighbors
    
    del graph[v]  # Remove v from the graph
    
    # Step 3: remove self-loops
    graph[u] = [x for x in graph[u] if x != u]
    
    # now recursively call the function on the updated graph
    return karger_min_cut(graph)


def run_karger_multiple_times(graph, iterations):
    """
    Runs Karger's algorithm multiple times to improve the probability of finding the true minimum cut.

    Args:
        graph (dict): An adjacency list representation of the graph.
        iterations (int): Number of times to run the algorithm.
    
    Returns:
        int: The minimum cut found across all iterations.
    """
    min_cut = float('inf')
    for _ in range(iterations):
        # Make a deep copy of the graph for each iteration
        graph_copy = {node: neighbors[:] for node, neighbors in graph.items()}
        cut = karger_min_cut(graph_copy)
        min_cut = min(min_cut, cut)
    return min_cut