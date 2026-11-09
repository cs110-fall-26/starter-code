def read_file(filename):
    contents = []
    # TODO do together
    return contents
    

def get_words(file_contents):
    words = {}
    # TODO Implement me!
    return words 

def find_max(words):
    largest = {"word":"", "occurrence":0}
    for (word, occurrence) in words.items():
        if occurrence > largest["occurrence"]:
            largest["occurrence"] = occurrence
            largest["word"] = word
    return largest

def find_second_largest(words):
    largest = find_max(words)
    words = dict(words)
    words.pop(largest['word'])
    return find_max(words)

def main():
    words = get_words(read_file("gutenberg_alice.txt"))
    largest = find_max(words)
    second_largest = find_second_largest(words)
    print(f"Most common: {largest}")
    print(f"Second most common: {second_largest}")

if __name__ == "__main__":
    main()

