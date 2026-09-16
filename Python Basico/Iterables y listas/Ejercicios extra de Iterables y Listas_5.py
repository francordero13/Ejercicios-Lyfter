
words=[]

for i in range(5):
    word= input(f"Ingrese la palaba {i+1}: ")
    words.append(word)

new_list=[]

for word in words:
    if len(word)>4:
        new_list.append(word)

print("Lista original: ", words)
print("Lista con palabras mayores a 4 letras: ",new_list)