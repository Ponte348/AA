import os

def getStats(filename, n=20):
    """Go to the stats directories and get the stats for the given book.
    The files are all organized in the same way:
    - Actual words start in line 6 (index 5)
    - Format is "word: count"
    - Words are sorted by count, highest to lowest    

    Args:
        filename (string): book to be read (must include .txt)
        n (int): number of lines to read
        
    Returns:
        list, list, list: exhaustive stats, probabilistic stats, streaming stats
    """
    # read exhaustive
    with open(os.path.join("exhaustive_wc_stats", filename), 'r') as f:
        ex_lines = f.readlines()[5:n+5]  # Skip header, get n lines
        ex_stats = [line.split(':')[0].strip() for line in ex_lines]
        
    # read probabilistic    
    with open(os.path.join("prob_decreasing_stats", filename), 'r') as f:
        prob_lines = f.readlines()[5:n+5]
        prob_stats = [line.split(':')[0].strip() for line in prob_lines]
        
    # read streaming  
    with open(os.path.join("streaming_stats", filename), 'r') as f:
        stream_lines = f.readlines()[5:n+5]
        stream_stats = [line.split(':')[0].strip() for line in stream_lines]
        
    return ex_stats, prob_stats, stream_stats

def topN(n=20, ex=None, prob=None, stream=None):
    """Takes the top n values from each list and compares them.
    This is done by going through the first n values of ex and checking
    how many of them are in prob and stream. 

    Args:
        ex (list): list with exhaustive counts
        prob (list): list with probabilistic counts
        stream (list): list with streaming counts
        n (int, optional): will check top n values
        
    Returns:
        float, float: percentage of prob in ex, percentage of stream in ex
    """
    if not all([ex, prob, stream]):
        return 0, 0
        
    # take first n words from each list
    ex_set = set(ex[:n])
    prob_set = set(prob[:n])
    stream_set = set(stream[:n])
    
    # use intersection to find matches
    prob_matches = len(ex_set.intersection(prob_set))
    stream_matches = len(ex_set.intersection(stream_set))
    
    # calc accuracy
    accuracy_prob = prob_matches / n * 100
    accuracy_stream = stream_matches / n * 100
    
    return accuracy_prob, accuracy_stream

if __name__ == "__main__":
    ex_stats, prob_stats, stream_stats = getStats("Don Quixote.txt")
    
    N_values = [3, 5, 10, 15, 20, 25, 30, 40, 50]
    
    for i in N_values:
        accuracy_prob, accuracy_stream = topN(i, ex_stats, prob_stats, stream_stats)
        print(f"Top-{i} Accuracy of Probabilistic: {accuracy_prob:.2f}%")
        print(f"Top-{i} Accuracy of Streaming: {accuracy_stream:.2f}%")
        print()