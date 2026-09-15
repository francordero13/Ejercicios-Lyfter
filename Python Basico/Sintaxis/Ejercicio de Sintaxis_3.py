
## Ejercicio con numero secreto escogido por mi
#num_secret=3
#num=int(input("Ingrese un numero del 1 al 10: "))
#while num != num_secret:
    #print("No es el numero secreto, vuelva a intentarlo")
    #num=int(input("Ingrese un numero del 1 al 10: "))
#print("adivinó el numero secreto, felicidades")




import random
num_secret=random.randint(1,10)
num=int(input("Ingrese un numero del 1 al 10: "))
while num != num_secret:
    print("No es el numero secreto, vuelva a intentarlo")
    num=int(input("Ingrese un numero del 1 al 10: "))
print("adivinó el numero secreto, felicidades")