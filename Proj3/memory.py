import psutil
import os
from time import perf_counter_ns
from exhaustive_wc import countWordOccurrences
from probablistic_wc import probabilisticDecreasingCount
from streaming_wc import lossyCount

def get_memory_usage():
    """Get current memory usage in kB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024  # kB

def measure_memory_and_time(func, *args):
    """Measure memory and time used by function"""
    initial_memory = get_memory_usage()
    start_time = perf_counter_ns()
    
    func(*args)
    
    end_time = perf_counter_ns()
    final_memory = get_memory_usage()
    
    return final_memory - initial_memory, (end_time - start_time) / 1e9  # Convert ns to seconds

def compare_memory_and_time_usage(filename):
    print(f"Memory and time usage for {filename}:")
    print("-" * 50)
    
    # measure each algorithm
    #exhaustive_mem, exhaustive_time = measure_memory_and_time(countWordOccurrences, filename)
    #print(f"\n               Memory      Time")
    #print(f"Exhaustive:    {exhaustive_mem:.2f} kB, {exhaustive_time:.2f} seconds\n\n")
    #
    #prob_mem, prob_time = measure_memory_and_time(probabilisticDecreasingCount, filename)
    #print(f"\n               Memory      Time")
    #print(f"Probabilistic: {prob_mem:.2f} kB, {prob_time:.2f} seconds\n\n")
    
    stream_mem, stream_time = measure_memory_and_time(lossyCount, filename)
    print(f"\n               Memory      Time")
    print(f"Streaming:     {stream_mem:.2f} kB, {stream_time:.2f} seconds\n\n")

if __name__ == "__main__":
    #filename = "processedFiles/Don Quixote.txt"
    #compare_memory_and_time_usage(filename)
    
    #files = ["processedFiles/Don Quixote.txt", "processedFiles/aleatorios000500000.txt", "processedFiles/aleatorios001000000.txt", "processedFiles/aleatorios005000000.txt"]
    #files = ["processedFiles/5000000bigfile.txt", "processedFiles/7500000bigfile.txt"] #, "processedFiles/10000000bigfile.txt"]
    files = ["processedFiles/10000000bigfile.txt"]
    for file in files:
        compare_memory_and_time_usage(file)
        print()