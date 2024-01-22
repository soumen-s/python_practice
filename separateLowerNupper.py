# Program to arrange string characters such that lowercase letters should come first

str1 = input("Enter a string: ")
print('\nOriginal String:', str1)

lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)  #for lowercase characters
    else:
        upper.append(char)  #for uppercase characters

# Joining
sorted_str = ''.join(lower + upper)

print('Result:', sorted_str)
