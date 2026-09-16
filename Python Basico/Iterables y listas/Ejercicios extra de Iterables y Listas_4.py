my_list = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

average= sum(my_list)/len(my_list)
newlist=[]


for num in my_list:
    if num>average:
        newlist.append(num)


print("Promedio: ",average)
print("Nueva lista: ",newlist)