

numbers=[]
for i in range (10):
    num = int(input("Ingrese un numero: "))
    numbers.append(num)
print("Numeros ingresados: ", numbers)

m=numbers[0]

for n in numbers:
    if n > m:
        m=n

print("Numero mas alto: ", m)