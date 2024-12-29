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
            # decrease probability as word count increases
            prob = 1 / sqrt(2)**word_count[word]
            if random.random() <= prob:
                word_count[word] += 1
        else:
            word_count[word] = 1
            
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    stats_file = "prob_decreasing_stats/" + file.split("/")[-1]
    with open(stats_file, 'w') as f:
        f.write("Probabilistic decreasing count results\n")
        f.write("Total words processed: {}\n".format(len(words)))
        f.write("Probability: 1 / sqrt(2)^count\n\n")
        f.write("Word occurrences:\n")
        for word, count in sorted_words:
            f.write(f"{word}: {count}\n")
            
    print(f"Statistics saved to {stats_file}")

if __name__ == "__main__":
    files = getProcessedFiles()
    for file in files:
        probabilisticDecreasingCount(file)
        print()