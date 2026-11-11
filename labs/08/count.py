import sys

def read_file(filename):
    contents = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                contents.append(line)
    except FileNotFoundError:
        print("File not found!")
    return contents 

def get_word_count(contents):
    words = {}
    for line in contents:
        line = line.split(" ")
        for word in line:
            if word not in words:
                words[word] = 0
            words[word] += 1
    return words 

def most_common_word(word_count):
    largest = {"word":"", "occurrence":0}
    for (word, occurrence) in word_count.items():
        if occurrence > largest["occurrence"]:
            largest["occurrence"] = occurrence
            largest["word"] = word
    return largest

def main():
    # TODO Get command line argumnets
    # TODO Check if at least 2 arguments
    # TODO Filename should be in `args[1]`
    # TODO read file from filename, get word count of given file, print out most common word of this file.
    
if __name__ == "__main__":
    main()

