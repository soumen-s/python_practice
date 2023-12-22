# Program to find a Decimal value of a Binary number

def dec_to_binary(decimal_number):
    bin_form = bin(decimal_number)[2:]
    return bin_form

dec_input = int(input("Enter a decimal number: "))

bin_output = dec_to_binary(dec_input)

print(f"Binary representation of {dec_input} is: {bin_output}")