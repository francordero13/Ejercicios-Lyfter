
def funcion (practice):
    upper=0
    lower=0
    for letter in practice:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower+=1
    print(f"La cantidad de mayusculas son {upper} y la cantidad de minusculas son {lower}")

funcion(" I love nacion Sushi")