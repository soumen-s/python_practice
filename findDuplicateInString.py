# Program to check if a given string contains all unique characters or not

def is_unique(s):
    
    char_set = set()

    for char in s:

        if char in char_set:
            return False
        char_set.add(char)  #for tracking

    return True

s = input("\nEnter a string: ")
result = is_unique(s)

if result:
    print("\nThe string contains all unique characters.")
else:
    print("\nThe string contains duplicate characters.")
