number1=int(input("Ingresar numero 1: "))
number2=int(input("Ingresar numero 2: "))
number3=int(input("Ingresar numero 3: "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3) == 30:
    print("Correcto")
else:
    print("Incorrecto, ninguno da 30 ni la suma de los 3")
    