print ("----Simulador de ahorro-----")

name=input("Ingresa tu nombre")
monthly_savings=float(input("Cuantos dolares ahorras por mes"))
months=int(input("Cuantos meses deseas simular"))
total=0

for month in range (1,months+1):
    total= total+monthly_savings
    print(f"mes {month}: total acumulado={total}")

    print(f"{name}, en {months} meses habras ahorrado: {total}")