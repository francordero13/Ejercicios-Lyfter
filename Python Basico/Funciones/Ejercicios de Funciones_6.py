def funcion(text):
    list_1=text.split("-")
    list_1.sort()
    result="-".join(list_1)

    return(result)

print(funcion("python-variable-funcion-computadora-monitor"))
