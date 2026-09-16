my_list = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

positive=True

for list in my_list:
    if list<=0:
        positive=False
        break

if positive:
    print("Todos los elementos son positivos")
else:
    print("No todos los elementos son positivos")
    