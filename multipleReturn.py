# Program to show returning multiple variables from a single function

def calc(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    
    return addition, subtraction, multiplication, division  # return multiple values separated by comma

result = calc(40, 10)
print("The results are:",result) # tuple form