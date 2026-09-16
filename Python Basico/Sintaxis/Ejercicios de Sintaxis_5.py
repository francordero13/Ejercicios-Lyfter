quantity=int(input("Ingresar la cantidad de notas"))
approved=0
not_approved=0

sum_approved=0
sum_not_approved=0
sum_totalL=0

for i in range(quantity):
    note=float(input(f"Ingrese la nota {i+1}: "))
    sum_totalL+=note
    if note>70:
        approved+=1
        sum_approved+=note
    else:
        not_approved+=1
        sum_not_approved+=note
average=sum_totalL/quantity

if approved>0:
    approved_average=sum_approved/approved
else:
    approved_average= 0
if not_approved>0:
    not_approved_average=sum_not_approved/not_approved
else:
    not_approved_average= 0

print("Resulados")
print("Notas aprobadas: ", approved)
print("Notas no aprobadas: ", not_approved)
print("Promedio general: ", average)
print("Promedio de aprobadas: ", approved_average)
print("Promedio de las desaprobadas: ", not_approved_average)