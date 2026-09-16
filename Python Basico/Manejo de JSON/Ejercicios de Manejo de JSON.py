import json


def pokemon_program():
    with open("pokemones.json", "r", encoding="utf-8") as file:
        pokemones = json.load(file)

    name = input("Nombre del pokemon: ")
    type = input("Tipo de pokemon: ")
    level = int(input("Digite el nivel del pokemon: "))

    new_pokemon = {
        "name": name,
        "type": type,
        "level": level
    }

    pokemones.append(new_pokemon)

    with open("pokemones.json", "w", encoding="utf-8") as file:
        json.dump(pokemones, file, indent=4, ensure_ascii=False)

    print("El Pokemon fue agregado correctamente.")


pokemon_program()



