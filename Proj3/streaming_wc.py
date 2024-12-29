from file_processing import getProcessedFiles
import os

def lossyCount(file, epsilon=0.001):
    """Lossy Count Algorithm for word frequency estimation.  
    Follows https://en.wikipedia.org/wiki/Lossy_Count_Algorithm
    
    Args:
        file (str): Path to file to process
        epsilon (float): Error bound
    """
    with open(file, 'r') as f:
        text = f.read()
        lines = [line for line in text.splitlines() if line.strip()]
    
    words = ' '.join(lines).split()
    N = len(words)
    
    bucket_width = int(1/epsilon)
    word_count = {}
    
    # process stream
    for i, word in enumerate(words):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
        # at the end of each bucket
        if (i + 1) % bucket_width == 0:
            # decrement all counters by 1 and remove items ≤ 0
            word_count = {w: c-1 for w, c in word_count.items() if c > 1}
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    stats_file = os.path.join("lossy_count_stats", os.path.basename(file))
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
        lossyCount(file)