from file_processing import getProcessedFiles

from file_processing import getProcessedFiles
from math import sqrt
import random

def probabilisticDecreasingCount(file):
    print(f"Probabilistic decreasing count for {file}")
    
    with open(file, 'r') as f:
        text = f.read()
        lines = [line for line in text.splitlines() if line.strip()]
    
    words = ' '.join(lines).split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            # Probability decreases as count increases
            prob = 1 / sqrt(2)**word_count[word]
            if random.random() <= prob:
                word_count[word] += 1
        else:
            word_count[word] = 1
            
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    stats_file = "prob_decreasing_stats/" + file.split("/")[-1]
    with open(stats_file, 'w') as f:
        f.write("Word occurrences (probabilistic decreasing):\n")
        for word, count in sorted_words:
            f.write(f"{word}: {count}\n")
            
    print(f"Statistics saved to {stats_file}")

def lossyCount(file, epsilon=0.01):
    print(f"Lossy counting for {file} with epsilon {epsilon}")
    
    with open(file, 'r') as f:
        text = f.read()
        lines = [line for line in text.splitlines() if line.strip()]
    
    words = ' '.join(lines).split()
    N = len(words)
    bucket_width = int(1/epsilon)
    current_bucket = 1
    word_count = {}  # Stores (count, delta) tuples
    
    for i, word in enumerate(words):
        # Remove infrequent elements when moving to new bucket
        if i % bucket_width == 0 and i > 0:
            word_count = {w: (c, d) for w, (c, d) in word_count.items() 
                         if c + d > current_bucket}
            current_bucket += 1
            
        if word in word_count:
            count, delta = word_count[word]
            word_count[word] = (count + 1, delta)
        else:
            word_count[word] = (1, current_bucket - 1)
    
    # Convert to final counts and sort
    final_counts = {w: c for w, (c, _) in word_count.items()}
    sorted_words = sorted(final_counts.items(), key=lambda x: x[1], reverse=True)
    
    stats_file = "lossy_count_stats/" + file.split("/")[-1]
    with open(stats_file, 'w') as f:
        f.write(f"Lossy counting results (epsilon={epsilon}):\n")
        f.write(f"Total words processed: {N}\n")
        f.write(f"Bucket width: {bucket_width}\n\n")
        f.write("Word occurrences:\n")
        for word, count in sorted_words:
            f.write(f"{word}: {count}\n")
            
    print(f"Statistics saved to {stats_file}")

if __name__ == "__main__":
    files = getProcessedFiles()
    for file in files:
        probabilisticDecreasingCount(file)
        lossyCount(file)
        print()