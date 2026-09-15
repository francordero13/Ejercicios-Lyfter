import csv

def save_videogames():
    quantity = int(input("Cuantos videojuegos desea ingresar?"))

    with open ("videogames.csv", "w",newline="",encoding="utf-8") as file:
        writer1 = csv.writer(file,delimiter="\t")

        writer1.writerow(["nombre","genero","desarrollador","clasificacion"])

        for i in range (quantity):
            print(f"videogame {i+1}")

            name=input ("nombre: ")
            gender=input ("genero: ")
            coder=input ("desarollador: ")
            clasification=input ("clasificacion ESRB: ")

            writer1.writerow([
                name,
                gender,
                coder,
                clasification
            ])
    print("Los videojuegos fueron guardados correctamente. ")

save_videogames()