

full_list=list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

number=int(input(" Ingrese el numero que desea buscar: "))

count=full_list.count(number)
print(f"El {number} aparece {count} veces en la lista")
