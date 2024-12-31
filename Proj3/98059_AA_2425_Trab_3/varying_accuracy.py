import sys
from exhaustive_wc import countWordOccurrences
from probablistic_wc import probabilisticDecreasingCount
from streaming_wc import lossyCount
import os
from time import perf_counter_ns
import psutil

def get_memory_usage():
    """Get current memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

def measure_memory(func, *args):
    """Measure memory used by function"""
    initial_memory = get_memory_usage()
    func(*args)
    final_memory = get_memory_usage()
    return final_memory - initial_memory

def parse_stats_file(filepath):
    """Parse the stats file and return a dictionary of word counts"""
    word_counts = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if ":" in line:
            try:
                word, count = line.strip().split(': ')
                try:
                    count = float(count)
                    word_counts[word] = count
                except ValueError:
                    continue
            except ValueError:
                continue
                
    return word_counts

def get_exhaustive_topn(filepath, n=100):
    """Get true top N words from exhaustive count"""
    results = countWordOccurrences(filepath)
    stats_file = f"exhaustive_wc_stats/{os.path.basename(filepath)}"
    word_counts = parse_stats_file(stats_file)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_words[:n])

def calculate_accuracy(true_counts, estimated_counts):
    """Calculate accuracy between true and estimated top N counts"""
    true_words = set(true_counts.keys())
    estimated_words = set(estimated_counts.keys())
    common_words = true_words.intersection(estimated_words)
    return len(common_words) / len(true_words)

def test_probabilistic_runs(filepath="processedFiles/Don Quixote.txt", n=100):
    """Test probabilistic counter with different numbers of runs"""
    runs = [1, 5, 10, 20, 40, 60, 80, 100]
    true_counts = get_exhaustive_topn(filepath, n)
    
    print(f"\nTesting probabilistic counter with different run counts (N={n}):")
    print("-" * 80)
    print("Runs\tAccuracy\tExecution Time (ms)\tMemory Usage (MB)")
    print("-" * 80)
    
    accuracies = {}
    times = {}
    memories = {}
    for num_runs in runs:
        # time and measure memory of probabilistic counter
        start_time = perf_counter_ns()
        memory_usage = measure_memory(probabilisticDecreasingCount, filepath, num_runs)
        end_time = perf_counter_ns()
        execution_time = (end_time - start_time) / 1_000_000  # Convert ns to ms
        
        # read results
        stats_file = f"prob_decreasing_stats/{os.path.basename(filepath)}"
        estimated_counts = parse_stats_file(stats_file)
        
        # top N
        sorted_words = sorted(estimated_counts.items(), key=lambda x: x[1], reverse=True)
        top_n_counts = dict(sorted_words[:n])
        
        # accuracy
        accuracy = calculate_accuracy(true_counts, top_n_counts)
        accuracy = accuracy * 100
        accuracies[num_runs] = accuracy
        times[num_runs] = execution_time
        memories[num_runs] = memory_usage
        print(f"{num_runs}\t{accuracy:.0f}%\t\t{execution_time:.2f}\t\t{memory_usage:.2f}")
    
    return accuracies, times, memories

def test_streaming_epsilons(filepath="processedFiles/Don Quixote.txt", n=100):
    """Test streaming counter with different epsilon values"""
    epsilons = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]
    true_counts = get_exhaustive_topn(filepath, n)
    
    print(f"\nTesting streaming counter with different epsilon values (N={n}):")
    print("-" * 65)
    print("Epsilon\tAccuracy\tMemory Usage (MB)")
    print("-" * 65)
    
    accuracies = {}
    memories = {}
    for epsilon in epsilons:
        # run streaming counter and measure memory
        memory_usage = measure_memory(lossyCount, filepath, epsilon)
        
        # results
        stats_file = f"streaming_stats/{os.path.basename(filepath)}"
        estimated_counts = parse_stats_file(stats_file)
        
        # top N
        sorted_words = sorted(estimated_counts.items(), key=lambda x: x[1], reverse=True)
        top_n_counts = dict(sorted_words[:n])
        
        # accuracy
        accuracy = calculate_accuracy(true_counts, top_n_counts)
        accuracy = accuracy * 100
        accuracies[epsilon] = accuracy
        memories[epsilon] = memory_usage
        print(f"{epsilon:.4f}\t{accuracy:.0f}%\t\t{memory_usage:.2f}")
    
    return accuracies, memories

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "processedFiles/Don Quixote.txt"
    
    prob_accuracies, prob_times, prob_memories = test_probabilistic_runs(filepath)
    print()
    stream_accuracies, stream_memories = test_streaming_epsilons(filepath)