import json 

def num_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not a number")

def check_id_type(pokemon_id):
    try:
        return int(pokemon_id)
    except ValueError:
        return pokemon_id

def load_pokemon(filename):
    # TODO Do together
    pass

def get_pokemon(pokemon_list, pokemon_id):
    if type(pokemon_id) == int:
        if pokemon_id > 151 or pokemon_id < 1:
            return None 
        return pokemon_list[pokemon_id - 1]
    else:
        for pokemon in pokemon_list:
            if pokemon['name'] == pokemon_id:
                return pokemon 
        return None

def print_pokemon_data(pokemon):
    id = pokemon['id']
    name = pokemon['name']
    abilities_list = []
    for ability in pokemon['abilities']:
        abilities_list.append(ability['ability']['name'])
    moves_list = []
    for move in pokemon['moves']:
        moves_list.append(move['move']['name'])
    stats = {}
    for stat in pokemon['stats']:
        stats[stat['stat']['name']] = stat['base_stat']
    print(f"[{id}] {name}")
    print("Abilities:")
    for ability in abilities_list:
        print(f"- {ability}")
    print("Moves:")
    for move in moves_list:
        print(f"- {move}")
    for name, stat in stats.items():
        print(f"- {name}: {stat}")


def get_pokemon_ids(pokemon_list):
    pokemon_ids = {}
    # TODO Implement me!
    return pokemon_ids

def print_valid_pokemon(pokemon_ids):
    # TODO Implement me!

def options():
    print(f"Options:\n[1] View All Pokemon\n[2] View Specific Pokemon\n[3] Quit")

def main():
    pokemon_list = load_pokemon("pokemon.json")
    while True:
        options()
        user = num_input(">> ")
        if user == 1:
            valid_pokemon = get_pokemon_ids(pokemon_list)
            if valid_pokemon != None:
                print_valid_pokemon(valid_pokemon)
        elif user == 2:
            pokemon = input("Enter your pokemon id or name: ")
            pokemon = check_id_type(pokemon)
            pokemon_data = get_pokemon(pokemon_list, pokemon)
            if(pokemon_data != None):
                print_pokemon_data(pokemon_data)
        elif user == 3:
            return
        print()



   
if __name__ == "__main__":
    main()
