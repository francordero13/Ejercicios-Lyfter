def convertir_a_entero(lista):
    for i in lista:
        try:
            number=int(i)
            print(i, "Convertido a ", number)
        
        except ValueError:
            print("No se pudo convertir", i)

my_list=["4","hola,", "10", "5","adios"]
print("resultado")
convertir_a_entero(my_list)