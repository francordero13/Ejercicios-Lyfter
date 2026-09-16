def count_vowels(text):
    count = 0
    for letter in text:

        if letter.lower() in "aeiou":
            count += 1

    return count
my_text = input("Enter a text: ")
result = count_vowels(my_text)
print("Number of vowels:", result)