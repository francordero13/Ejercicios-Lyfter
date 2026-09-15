def my_text (text, character):
   count=0
   for word in text:
        if word==character:
           count=count+1
   return count
    
word_2= input("Ingrese alguna palabra a la que quiera poner a prueba: ")
word_3= input ("Ingrese el caracter que deseo buscar: ")
   
result=my_text(word_2,word_3)
print("el caracter, ", word_2, " aparece", result, " veces.")
