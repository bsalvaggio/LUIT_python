!/usr/bin/env python

# objective: build a dictionary that allows users to search for information about specific Pokémon such as their type, abilities, and stats

#create a dictionary to store data on each Pokemon 
pokemon_info = {
    "Bulbasaur": {"type": "Grass", "abilities": ["Overgrow", "chlorophyll"], "stats": [45, 49, 49, 65, 65, 45]},
    "Ivysaur": {"type": "Grass", "abilities": ["Overgrow", "Chlorophyll"], "stats": [60, 62, 63, 80, 80, 60]},
    "Venusaur": {"type": "Grass", "abilities": ["Overgrow", "Chlorophyll"],  "stats": [100, 100, 100, 100, 100, 100]},
}
...

#Create a function- 
#get_pokemon_info(pokemon_name) that takes and returns the information about that Pokémon

def get_pokemon_info(pokemon_name):
    if pokemon_name in pokemon_info:
        return pokemon_info[pokemon_name]
    else:
        return "Oops! Pokemon not found!"
        
# create a main function that takes user input and calls get_pokemon_info(pokemon_name) to get the information about the selected Pokémon. 
	
def main():
    pokemon_name = input("Enter a Pokemon name: ")
    info = get_pokemon_info(pokemon_name)
    if info != "Oops! Pokemon not found!":
        print("Type:", info["type"])
        print("Abilities:", ", ".join(info["abilities"]))
        print("Stats:", info["stats"])
    else:
        print(info)

if __name__ == "__main__":
    main()
	
