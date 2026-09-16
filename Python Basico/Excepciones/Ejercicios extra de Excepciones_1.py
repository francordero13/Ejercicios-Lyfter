def get_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero")

    return name

def get_age():

    try:
        age = int(input("Ingrese su edad: "))
        return age
    except ValueError:
        print("Numero no valido")
        return None

def show_result(name, age):
    print("Bienvenido, su nombre es:", name, "y su edad es", age)


def main():
    try:
        name = get_name()
        age = get_age()
        if age is not None:
            show_result(name, age)

    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()