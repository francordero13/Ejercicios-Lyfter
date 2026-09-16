import csv


num_games = int(input("¿Cuántos videojuegos desea ingresar? "))


with open("videogames.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)


    writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])


    for i in range(num_games):
        print(f"\nVideojuego #{i + 1}")

        name = input("Nombre: ")
        genre = input("Género: ")
        developer = input("Desarrollador: ")
        esrb_rating = input("Clasificación ESRB: ")

        writer.writerow([name, genre, developer, esrb_rating])

print("\nLos datos se guardaron correctamente en 'videogames.csv'.")