def filter_words(words, n):

    new_list = []
    for word in words:
        if len(word) > n:
            new_list.append(word)
    return new_list


my_list = ["cielo", "sol", "maravilloso", "dia"]
number = int(input("Enter the minimum number of letters: "))
result = filter_words(my_list, number)
print(result)