import os
import re
import nltk
from nltk.corpus import stopwords

def getOriginalFiles():
    files = []
    for file in sorted(os.listdir("originalFiles/")):
        files.append("originalFiles/" + file)
    return files

def getProcessedFiles():
    files = []
    for file in sorted(os.listdir("processedFiles/")):
        files.append("processedFiles/" + file)
    return files

def removeHeaderTail(file):
    """
    Files:
    ['originalFiles/Lusíadas English.txt', 'originalFiles/Metamorphosis.txt', 'originalFiles/Lusíadas.txt', 'originalFiles/Moby Dick.txt', 'originalFiles/Lusíadas Spanish.txt', 'originalFiles/Don Quixote.txt']
    """
    match(file):
        case "originalFiles/Lusíadas English.txt":
            print("Removing Header and Tail from Lusíadas English")
            with open(file, 'r') as f:
                lines = f.readlines()
            
            new_lines = lines[90:19650]
            
            new_file = "processedFiles/Lusíadas English.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")
            
        case "originalFiles/Metamorphosis.txt":
            print("Removing Header and Tail from Metamorphosis")
            with open(file, 'r') as f:
                lines = f.readlines()
            
            new_lines = lines[32:1903]
            
            new_file = "processedFiles/Metamorphosis.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")
            
        case "originalFiles/Lusíadas.txt":
            print("Removing Header and Tail from Lusíadas")
            with open(file, 'r') as f:
                lines = f.readlines()
            
            new_lines = lines[33:11079]
            
            new_file = "processedFiles/Lusíadas.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")
            
        case "originalFiles/Moby Dick.txt":
            print("Removing Header and Tail from Moby Dick")
            with open(file, 'r') as f:
                lines = f.readlines()
            
            new_lines = lines[27:21960]
            
            new_file = "processedFiles/Moby Dick.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")
            
        case "originalFiles/Lusíadas Spanish.txt":
            print("Removing Header and Tail from Lusíadas Spanish")
            with open(file, 'r') as f:
                lines = f.readlines()
            
            new_lines = lines[193:10466]
            
            new_file = "processedFiles/Lusíadas Spanish.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")
            
        case "originalFiles/Don Quixote.txt":
            print("Removing Header and Tail from Don Quixote")
            with open(file, 'r') as f:
                lines = f.readlines()
            
            new_lines = lines[606:42917]
            
            # aditionally for this one we need to remove lines with "photos"
            new_lines = [line for line in new_lines if ".jpg" not in line]
            new_lines = [line for line in new_lines if "Full Size" not in line]
            
            new_file = "processedFiles/Don Quixote.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")


def removePunctuationStopLower(file):
    print(f"Removing punctuation from {file}")
    with open(file, 'r') as f:
        lines = f.readlines()
    
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    for palavra in set(stopwords.words('portuguese')):
        stop_words.add(palavra)
    
    new_lines = []
    for line in lines:
        new_line = re.sub(r'[^\w\s]', '', line)
        new_line = new_line.lower()
        # remove all stop words
        new_line = ' '.join([word for word in new_line.split() if word not in stop_words])
        new_lines.append(new_line + '\n')
    
    new_file = "processedFiles/" + file.split("/")[1]
    with open(new_file, 'w') as f:
        f.writelines(new_lines)
    print(f"Processed file saved as {new_file}")
    
def main():
    files = getOriginalFiles()
    for file in files:
        removeHeaderTail(file)
        processed_file = "processedFiles/" + file.split("/")[1]
        removePunctuationStopLower(processed_file)
        
        print()
    
if __name__ == "__main__":
    main()