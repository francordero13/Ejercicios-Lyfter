my_list = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

mini=my_list[0]

for num in my_list:
    if num < mini:
        mini=num

print(" El numero mas peuqeño de la lista es: ",mini)