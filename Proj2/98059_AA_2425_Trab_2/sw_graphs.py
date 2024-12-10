from mincut import *

def load_graph(file_path):
    # load graph from the teacher files
    graph = nx.Graph()
    
    with open(file_path, 'r') as file:
        for line in file:
            nodes = line.split()
            graph.add_edge(int(nodes[0]), int(nodes[1]))

    return graph

def karger_graph(file_path):
    graph = load_graph(file_path)
    mincut = karger_min_cut(graph)
    return mincut

def tiny():
    file_path = "SW_ALGUNS_GRAFOS/SWtinyG.txt"
    mincut=0; time=0; n_tries=10
    for i in range(n_tries):
        start = perf_counter_ns()
        mincut+=karger_graph(file_path)[0]
        time += perf_counter_ns() - start
    
    visualize_min_cut(load_graph(file_path), karger_graph(file_path)[1], "tiny_min_cut_graph.png")
    
    print(f"Minimum cut for {file_path}: {mincut/n_tries}")
    print(f"Time taken: {round(time/n_tries/1e6, 2)} miliseconds")

def medium():
    file_path = "SW_ALGUNS_GRAFOS/SWmediumG.txt"
    mincut=0; time=0; n_tries=25
    for i in range(n_tries):
        start = perf_counter_ns()
        mincut+=karger_graph(file_path)[0]
        time += perf_counter_ns() - start
    
    visualize_min_cut(load_graph(file_path), karger_graph(file_path)[1], "medium_min_cut_graph.png")
    
    print(f"Minimum cut for {file_path}: {mincut/n_tries}")
    print(f"Time taken: {round(time/n_tries/1e9, 2)} seconds")

def large():
    file_path = "SW_ALGUNS_GRAFOS/SWlargeG.txt"
    start_time = perf_counter_ns()
    # for this one we'll just do one try since it's a very large graph
    mincut, partitions = karger_graph(file_path)
    end_time = perf_counter_ns()
    
    visualize_min_cut(load_graph(file_path), partitions, "large_min_cut_graph.png")
    print(f"Minimum cut for {file_path}: {mincut}")
    print(f"Time taken: {round((end_time-start_time)/1e9, 2)} seconds")

if __name__ == '__main__':
    tiny()
    medium()
    large()