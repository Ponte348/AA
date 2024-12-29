from file_processing import getProcessedFiles
from math import sqrt
import random
import os
from collections import defaultdict

def probabilisticDecreasingCount(file, num_runs=10):
    print(f"Probabilistic decreasing count for {file} ({num_runs} runs)")
    
    # Read file once
    with open(file, 'r') as f:
        text = f.read()
        lines = [line for line in text.splitlines() if line.strip()]
    
    words = ' '.join(lines).split()
    total_counts = defaultdict(float)  # Use float for averaging
    
    # Run multiple times
    for run in range(num_runs):
        word_count = {}
        
        for word in words:
            if word in word_count:
                prob = 1 / sqrt(2)**word_count[word]
                if random.random() <= prob:
                    word_count[word] += 1
            else:
                word_count[word] = 1
                
        # Add this run's counts to total
        for word, count in word_count.items():
            total_counts[word] += count
    
    # Calculate averages
    avg_counts = {word: count/num_runs for word, count in total_counts.items()}
    sorted_words = sorted(avg_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Create directory if it doesn't exist
    os.makedirs("prob_decreasing_stats", exist_ok=True)
    
    # Save results
    stats_file = os.path.join("prob_decreasing_stats", os.path.basename(file))
    with open(stats_file, 'w') as f:
        f.write(f"Probabilistic decreasing count results (averaged over {num_runs} runs)\n")
        f.write(f"Total words processed: {len(words)}\n")
        f.write("Probability: 1 / sqrt(2)^count\n\n")
        f.write("Average word occurrences:\n")
        for word, avg_count in sorted_words:
            f.write(f"{word}: {avg_count:.1f}\n")
            
    print(f"Statistics saved to {stats_file}")

if __name__ == "__main__":
    files = getProcessedFiles()
    for file in files:
        probabilisticDecreasingCount(file)
        print()