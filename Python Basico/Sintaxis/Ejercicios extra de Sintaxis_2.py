time=int(input("Ingrese el tiempo en segundos: "))
if time>600:
    result="mayor"
elif time==600:
    result= "igual"
else:
    result=600-time
print(result)