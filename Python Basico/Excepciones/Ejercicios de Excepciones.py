def my_sum(actual, number):
    return actual + number

def subtraction(actual, number):
    return actual - number

def multiplication(actual, number):
    return actual * number

def division(actual, number):
    if number == 0:
        print("No se puede dividir entre 0")
        return actual

    return actual / number

def delete():
    return 0

def main():

    number_actual = 0

    while True:

        print("\nNumero actual:", number_actual)

        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Borrar")

        option = input("Seleccione una opcion: ")

        try:

            if option == "1":
                number = float(input("Digite un numero: "))
                number_actual = my_sum(number_actual, number)

            elif option == "2":
                number = float(input("Digite un numero: "))
                number_actual = subtraction(number_actual, number)

            elif option == "3":
                number = float(input("Digite un numero: "))
                number_actual = multiplication(number_actual, number)

            elif option == "4":
                number = float(input("Digite un numero: "))
                number_actual = division(number_actual, number)

            elif option == "5":
                number_actual = delete()

            else:
                print("Error: opcion invalida")

        except ValueError:
            print("Error: debe ingresar un numero valido")

if __name__ == "__main__":
    main()