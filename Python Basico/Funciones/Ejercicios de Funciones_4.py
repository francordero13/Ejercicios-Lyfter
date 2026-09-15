def funcion_2 (word):
    new_word=""

    for i in range(len(word)-1,-1,-1):
        new_word+=word[i]

    return new_word
print(funcion_2("Hola"))