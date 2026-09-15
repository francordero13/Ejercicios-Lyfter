print("------Clasificador de nivel Gamer")
name = input("Ingresa tu nombre: ")
hours = int(input("Ingrese la cantidad de horas jugadas: "))
is_competitive=input("Jugas competitivo? (si/no)")

if hours<10:
    category="Novato"
    message= "Bienvenido al mundo gamer"
elif hours<50:
    category="casual"
    message= "Ya le estas agarrando ritmo"
elif hours <200:
    category="Gamer"
    message= "Definitivamente sabes lo que haces"
elif hours >=200 and is_competitive == "si":
    category="Pro"
    message= "Eres una leyenda"
else:
    category="Gamer"
    message= "Tienes la experiencia, pero aun no entras al competitivo"
print(name, "Tu categoria es: ", category)
print(message)