def suma_valores(lista):
    actual=0
    for i in lista:
        try:
            number=float(i)
            print(i, "convertido a " , number)
            actual= actual+number
            
        
        except ValueError:
            print("Elemento Invalido:", i)
            
    print("Valor sumado correctamente: ",actual)

my_list=["4.5","hola", "10", "5","adios"]
print("resultado")
suma_valores(my_list)
