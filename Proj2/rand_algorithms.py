import random
import time
import networkx as nx

def karger_min_cut(graph):
    """
    Calculates the minimum cut of a graph using Karger's Randomized Algorithm.

    Args:
        graph (networkx.Graph): The graph object.

    Returns:
        int: The minimum cut (number of crossing edges).
        tuple: The two partitions of the graph.
    """
    graph = graph.copy()
    n = len(graph.nodes)

    # Track the partitions
    partitions = {node: {node} for node in graph.nodes}

    # Perform edge contractions until only 2 nodes remain
    while len(graph.nodes) > 2:
        # Step 1: Randomly pick an edge (u, v)
        u, v = random.choice(list(graph.edges))

        # Step 2: Contract the edge (u, v)
        # Merge node v into node u
        for neighbor in list(graph.neighbors(v)):
            if neighbor != u:
                graph.add_edge(u, neighbor)

        # Merge partitions
        partitions[u].update(partitions[v])
        del partitions[v]

        # Remove node v and all edges associated with it
        graph.remove_node(v)

    # Step 3: Return the number of edges between the two remaining nodes
    remaining_nodes = list(graph.nodes)
    partition_1 = partitions[remaining_nodes[0]]
    partition_2 = partitions[remaining_nodes[1]]
    min_cut = graph.size()

    return min_cut, (partition_1, partition_2)


def run_karger_multiple_times(graph, iterations):
    """
    Runs Karger's algorithm multiple times to improve the probability of finding the true minimum cut.

    Args:
        graph (networkx.Graph): The graph object.
        iterations (int): Number of times to run the algorithm.

    Returns:
        int: The minimum cut found across all iterations.
        tuple: The partitions corresponding to the minimum cut.
    """
    min_cut = float('inf')
    best_partitions = None

    for _ in range(iterations):
        graph_copy = graph.copy()
        cut, partitions = karger_min_cut(graph_copy)
        if cut < min_cut:
            min_cut = cut
            best_partitions = partitions

    return min_cut, best_partitions



def stoer_wagner_min_cut(graph):
    """
    Calculates the minimum cut of a graph using the Stoer-Wagner algorithm.

    Args:
        graph (networkx.Graph): The graph object.

    Returns:
        int: The minimum cut (number of crossing edges).
        tuple: The two partitions of the graph that form the minimum cut.
    """
    graph = graph.copy()
    min_cut = float('inf')
    best_partition = None

    # Track partitions during merging
    partitions = {node: {node} for node in graph.nodes}

    while graph.number_of_nodes() > 1:
        # Initialize variables
        nodes = list(graph.nodes)
        a = nodes[0]
        A = {a}  # Set of merged nodes
        W = {node: 0 for node in graph.nodes}  # Weights of nodes in A
        last_added_node = None

        # Phase 1: Grow the set A until it contains all nodes
        while len(A) < graph.number_of_nodes():
            # Find the most tightly connected node outside A
            most_tightly_connected_node = max(
                (node for node in graph.nodes if node not in A),
                key=lambda node: W[node],
            )
            A.add(most_tightly_connected_node)
            last_added_node = most_tightly_connected_node

            # Update weights of neighbors
            for neighbor in graph.neighbors(most_tightly_connected_node):
                if neighbor not in A:
                    W[neighbor] += 1  # Unweighted edge = 1

        # Phase 2: Calculate the cut value for the partition
        cut_value = sum(1 for neighbor in graph.neighbors(last_added_node))
        if cut_value < min_cut:
            min_cut = cut_value
            # Create the partitions
            partition_1 = partitions[last_added_node]
            partition_2 = set(graph.nodes) - partition_1
            best_partition = (partition_1, partition_2)

        # Phase 3: Merge the last added node into the second-to-last node
        second_last_node = list(A - {last_added_node})[-1]
        for neighbor in list(graph.neighbors(last_added_node)):
            if neighbor != second_last_node:
                graph.add_edge(second_last_node, neighbor)  # Merge edges
        graph.remove_node(last_added_node)

        # Update partitions
        partitions[second_last_node].update(partitions[last_added_node])
        del partitions[last_added_node]

    return min_cut, best_partition