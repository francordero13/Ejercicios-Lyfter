num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))
num3=int(input("Ingrese numero 3: "))

if num1 >= num2 and num1 >= num3:
    print("El mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El mayor es:", num2)
else:
    print("El mayor es:", num3)