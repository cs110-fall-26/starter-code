import sys
import requests 
import json

def define(word):
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    return requests.get(url).json()

def print_meanings(original_definition):
    meanings = original_definition.get("meanings")
    for meaning in meanings:
        print(f"Part of Speech: {meaning.get('partOfSpeech')}")
        print("Definitions:")
        for definition in meaning.get("definitions"):
            print(f"\tDefinition: {definition.get('definition')}")
            if(len(definition.get("synonyms", [])) > 0):
                print("\t\tSynonyms:")
                for synonym in definition.get("synonyms"):
                    print(f"\t\t\t- {synonym}")
            if(len(definition.get("antonyms", [])) > 0):
                print("\t\tAntonyms:")
                for antonym in definition.get("antonyms"):
                    print(f"\t\t\t- {antonym}")
        if(len(meaning.get("synonyms", [])) > 0):
            print("\tSynonyms:")
            for synonym in meaning.get("synonyms"):
                print(f"\t\t- {synonym}")
        if(len(meaning.get("antonyms", [])) > 0):
            print("\tAntonyms:")
            for antonym in meaning.get("antonyms"):
                print(f"\t\t- {antonym}")
        print()

def format_data(definition):
    return json.dumps(definition, indent=1)

def get_synonyms(definition):
    synonyms = []
    # TODO Implement me
    return synonyms

def get_antonyms(definition):
    antonyms = []
    # TODO Implement me
    return antonyms

def get_meanings(definition):
    meanings = []
    # TODO Implement me
    return meanings

def print_group(group_name, group):
    print(f"{group_name}:")
    for val in group:
        print(f"\t- {val}")

def main():
    if len(sys.argv) < 2:
        print(f"Invalid usage: python3 {sys.argv[0]} <word> <clean=default, raw, meaning, synonyms, antonyms>")
        return 
    word = sys.argv[1]
    definition = define(word)[0]
    print(f"Word: {word}")
    out_type = "clean"
    if(len(sys.argv) == 3):
        out_type = sys.argv[2]
    if out_type == "clean":
        print_meanings(definition)
    elif out_type == "raw":
        print(format_data(definition))
    elif out_type == "meaning": 
        print_group("Meanings", get_meanings(definition))
    elif out_type == "synonyms":
        print_group("Synonyms", get_synonyms(definition))
    elif out_type == "antonyms":
        print_group("Antonyms", get_antonyms(definition))
    else:
        print("Invalid type, defaulting to clean output")
        print_meanings(definition)



if __name__ == "__main__":
    main()

