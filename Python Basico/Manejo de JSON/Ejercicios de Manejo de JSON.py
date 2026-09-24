import json


def load_pokemons():
    with open("pokemones.json", "r", encoding="utf-8") as file:
        pokemones = json.load(file)
    return pokemones


def get_pokemon_data():
    name = input("Nombre del pokemon: ")
    pokemon_type = input("Tipo de pokemon: ")
    level = int(input("Digite el nivel del pokemon: "))
    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level
    }

    return new_pokemon


def add_pokemon(pokemones, new_pokemon):
    pokemones.append(new_pokemon)
    return pokemones


def save_pokemons(pokemones):
    with open("pokemones.json", "w", encoding="utf-8") as file:
        json.dump(pokemones, file, indent=4, ensure_ascii=False)


def pokemon_program():
    pokemones = load_pokemons()
    new_pokemon = get_pokemon_data()
    pokemones = add_pokemon(pokemones, new_pokemon)
    save_pokemons(pokemones)
    print("El Pokemon fue agregado correctamente.")


pokemon_program()




