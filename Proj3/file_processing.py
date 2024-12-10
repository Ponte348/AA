import os

def getFiles():
    files = []
    for file in sorted(os.listdir("originalFiles/")):
        files.append("originalFiles/" + file)
    return files
    
def removeHeaderTail(file):
    """
    Files:
    ['originalFiles/Lusíadas English.txt', 'originalFiles/Metamorphosis.txt', 'originalFiles/Lusíadas.txt', 'originalFiles/Moby Dick.txt', 'originalFiles/Lusíadas Spanish.txt', 'originalFiles/Don Quixote.txt']
    """
    match(file):
        case "originalFiles/Lusíadas English.txt":
            print("Removing Header and Tail from Lusíadas English")
            # open the file, remove the header and tail and save a new file
            with open(file, 'r') as f:
                lines = f.readlines()
            print(lines)
            # Assuming header is the first line and tail is the last line
            new_lines = lines[90:19650]
            
            new_file = "processedFiles/Lusíadas English.txt"
            with open(new_file, 'w') as f:
                f.writelines(new_lines)
            print(f"Processed file saved as {new_file}")
            
        case "originalFiles/Metamorphosis.txt":
            print("Removing Header and Tail from Metamorphosis")
        case "originalFiles/Lusíadas.txt":
            print("Removing Header and Tail from Lusíadas")
        case "originalFiles/Moby Dick.txt":
            print("Removing Header and Tail from Moby Dick")
        case "originalFiles/Lusíadas Spanish.txt":
            print("Removing Header and Tail from Lusíadas Spanish")
        case "originalFiles/Don Quixote.txt":
            print("Removing Header and Tail from Don Quixote")
    
def main():
    files = getFiles()
    for file in files:
        removeHeaderTail(file)
    
if __name__ == "__main__":
    main()