my_list=[4,3,6,1,7]
i= my_list[0]


my_list[0]=my_list[len(my_list)-1] #aqui estoy diciendo que la posicion 0 me va a pasar al ultimo lugar de mi lista
my_list[len(my_list)-1] = i
print(my_list)

