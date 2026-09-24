
import csv
def get_videogame():
    name = input("Nombre: ")
    gender = input("Género: ")
    coder = input("Desarrollador: ")
    classification = input("Clasificación ESRB: ")

    return [name, gender, coder, classification]

def save_videogames(videogames):
    with open("videogames.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])

        for videogame in videogames:
            writer.writerow(videogame)

def videogame_program():
    quantity = int(input("¿Cuántos videojuegos desea ingresar? "))

    videogames = []

    for i in range(quantity):
        print(f"\nVideojuego {i + 1}")

        videogame = get_videogame()
        videogames.append(videogame)

    save_videogames(videogames)

    print("Los videojuegos fueron guardados correctamente.")


videogame_program()


