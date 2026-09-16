name=input("Ingrese su nombre: ")
last_name=input("Ingrese su apellido: ")
age=int(input("Ingrese su edad"))

if age<3:
    print("Usted es un bebe")
elif age<11:
    print("Usted es un niño")
elif age<15:
    print("Usted es un Preadolecente")
elif age<21:
    print("Usted es un adolecente")
elif age<30:
    print("Usted es un adultojoven")
elif age<40:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")