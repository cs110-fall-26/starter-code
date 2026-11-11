import sys

def get_leet_equivalent(character):
    chars = {
        "A": "4",
        "B": "8",
        "C": "(",
        "D": ")",
        "E": "3",
        "F": "|=",
        "G": "6",
        "H": "#",
        "I": "1",
        "J": "]",
        "K": "|<",
        "L": "|_",
        "M": "|\\/|",
        "N": "|\\|",
        "O": "0",
        "P": "|o",
        "Q": "()_",
        "R": "I2",
        "S": "5",
        "T": "7",
        "U": "|_|",
        "V": "\\/",
        "W": "\\/\\/",
        "X": "><",
        "Y": "`/",
        "Z": "2"
    }
    return chars.get(character, character)

def read_file(filename):
    contents = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                contents.append(line)
    except FileNotFoundError:
        print("File not found.")
    return contents 

def write_file(contents, filename):
    with open(filename, 'w') as f:
        for line in contents:
            for word in line:
                f.write(word)
                f.write(" ")
            f.write("\n")

def get_inputs():
    contents = []
    print("Enter your words below. To stop, enter \"exit\".")
    while True:
        user = input(">> ")
        if user == "exit":
            return contents 
        contents.append(user)

def convert_contents(contents):
    contents = list(contents)
    for i in range(len(contents)):
        contents[i] = contents[i].split(" ")
        for j in range(len(contents[i])):
            contents[i][j] = convert_word(contents[i][j])
    return contents


def convert_word(word):
    # TODO Implement me
        

def main():
    # TODO Implement me 

if __name__ == "__main__":
    main()


