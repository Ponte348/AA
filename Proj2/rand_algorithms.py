import random
import time
import networkx as nx

def karger_min_cut(graph):
    """
    Calculates the minimum cut of an unweighted graph using Karger's Randomized Algorithm.

    Args:
        graph (networkx.Graph): The graph object.

    Returns:
        int: The minimum cut (number of crossing edges).
        int: Number of operations performed.
    """
    graph = graph.copy()
    operations = 0

    # Perform edge contraction until only 2 nodes remain
    while graph.number_of_nodes() > 2:
        # Step 1: Randomly pick an edge (u, v)
        u, v = random.choice(list(graph.edges))
        operations += 1

        # Step 2: Contract the edge (u, v)
        # Merge node v into node u
        for neighbor in list(graph.neighbors(v)):
            operations += 1
            if neighbor != u:  # Avoid self-loops
                graph.add_edge(u, neighbor)

        # Remove node v and all edges associated with it
        graph.remove_node(v)

    # Step 3: Return the number of edges between the two remaining nodes
    min_cut = graph.size()
    return min_cut, operations


def run_karger_multiple_times(graph, iterations):
    """
    Runs Karger's algorithm multiple times to improve the probability of finding the true minimum cut.

    Args:
        graph (networkx.Graph): The graph object.
        iterations (int): Number of times to run the algorithm.

    Returns:
        int: The minimum cut found across all iterations.
        float: Total execution time.
        int: Total number of operations performed.
    """
    min_cut = float('inf')
    total_operations = 0
    start_time = time.time()

    for _ in range(iterations):
        cut, operations = karger_min_cut(graph)
        total_operations += operations
        min_cut = min(min_cut, cut)

    execution_time = time.time() - start_time
    return min_cut, execution_time, total_operations



def stoer_wagner_min_cut(graph):
    """
    Calculates the minimum cut of an unweighted graph using the Stoer-Wagner algorithm.

    Args:
        graph (networkx.Graph): The graph object.

    Returns:
        int: The minimum cut (number of crossing edges).
        int: Number of operations performed.
    """
    graph = graph.copy()
    min_cut = float('inf')
    total_operations = 0

    while graph.number_of_nodes() > 1:
        # Step 1: Start with an arbitrary node
        nodes = list(graph.nodes)
        a = nodes[0]
        A = {a}
        W = {a: 0}  # Weights of nodes in A
        total_operations += 1

        while len(A) < graph.number_of_nodes():
            # Step 2: Find the most tightly connected node outside A
            most_tightly_connected_node = max(
                (node for node in graph.nodes if node not in A),
                key=lambda node: W.get(node, 0),
            )
            A.add(most_tightly_connected_node)

            # Update weights of neighbors
            for neighbor in graph.neighbors(most_tightly_connected_node):
                total_operations += 1
                if neighbor not in A:
                    W[neighbor] = W.get(neighbor, 0) + 1  # Unweighted edge = 1

            # Store the last added node
            last_node = most_tightly_connected_node

        # Cut value is the sum of edges connecting last_node
        cut_value = sum(1 for neighbor in graph.neighbors(last_node))
        min_cut = min(min_cut, cut_value)

        # Merge last_node into the second-to-last node
        second_last_node = list(A - {last_node})[-1]
        for neighbor in graph.neighbors(last_node):
            if neighbor != second_last_node:
                if graph.has_edge(second_last_node, neighbor):
                    # Merge edges (unweighted, so no weight addition needed)
                    pass
                else:
                    graph.add_edge(second_last_node, neighbor)

        graph.remove_node(last_node)

    return min_cut, total_operations