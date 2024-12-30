from file_processing import getProcessedFiles

def countWordOccurrences(file, stats_dir="exhaustive_wc_stats"):
    print(f"Counting word occurrences in {file}")
    
    with open(file, 'r') as f:
        text = f.read()
        lines = [line for line in text.splitlines() if line.strip()]
    
    # basic metrics
    num_lines = len(lines)
    words = ' '.join(lines).split()
    num_words = len(words)
    num_chars = sum(len(line) for line in lines)
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # sort by number of occurrences (highest to lowest)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # save stats
    stats_file = stats_dir + "/" + file.split("/")[-1]
    with open(stats_file, 'w') as f:
        f.write(f"Number of lines (excluding empty): {num_lines}\n")
        f.write(f"Number of words: {num_words}\n")
        f.write(f"Number of characters (excluding newlines): {num_chars}\n\n")
        f.write("Word occurrences:\n")
        for word, count in sorted_words:
            f.write(f"{word}: {count}\n")
    
    print(f"Statistics saved to {stats_file}")


if __name__ == "__main__":
    files = getProcessedFiles()
    for file in files:
        countWordOccurrences(file)
        print()