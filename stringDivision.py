# Program to find number of characters, digits and symbols in a string

def divided(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    
    for char in input_str:
        if char.isalpha():
            char_count += 1
            
        elif char.isdigit():
            digit_count += 1
            
        else:                   # if it is not letter or digit then it is special symbol
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbols =", symbol_count)

string = input("Enter a string: ")
print("Total counts of chars, digits, and symbols:\n")
divided(string)