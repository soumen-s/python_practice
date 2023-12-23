# Python program that takes name as input, removes all vowels from your name and display it

name = input("Enter your name: ")

name_without_vowels = ""  # To initialize an empty string

for char in name: 
    if char.lower() not in "aeiou":
        name_without_vowels += char


print("The name without vowels:", name_without_vowels)