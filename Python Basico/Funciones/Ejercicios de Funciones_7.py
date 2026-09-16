def funcion (numbers): 

    if numbers<2:
        return False
    
    for i in range(2, numbers):
        if numbers%i==0:
            return False
    
    return True

def funcion_2 (numbers_2): 
    numbers_3=[]
    for numbers_4 in numbers_2:
        if funcion(numbers_4):
            numbers_3.append(numbers_4)
    return numbers_3

new_list=[1,4,6,7,13,9,67]
print(funcion_2(new_list))