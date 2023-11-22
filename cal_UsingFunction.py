# Program to apply some operations(using function) using 2 user defined variables

'''
def create():    
    op1 = int(input("Enter the first number: "))
    global char
    char = input("Enter the operation (+, -, *, /, %): ")
    op2 = int(input("Enter the second number: "))
    return op1,op2
'''

def addition(x,y):
    print(f"The sum of {x} and {y} is : ",str(x+y)) # just like C  

def subtraction(x,y):
    print(f"The subtraction of {x} and {y} is : ",str(x-y))

def multiplication(op1, op2):
    print(f"The multiplication of {op1} and {op2} is : ",str(op1 * op2))

def division(op1, op2):
    print(f"The division of {op1} and {op2} is : ",str(op1 / op2))

def remainder(op1, op2):
    print(f"The remainder of {op1} and {op2} is : ",str(op1 % op2))

# ------------------------------------------------------

'''
#op1, op2 = create()
when we will return any number of value from a functon, to store that 
returned value we have to use that number of variables to store those values
'''
op1 = float(input("Enter the first number: "))
global char
char = input("Enter the operation (+, -, *, /, %): ")
op2 = float(input("Enter the second number: "))


if char == '+':
    addition(op1, op2)

elif char == '-':
    subtraction(op1, op2)

elif char == '*':
    multiplication(op1, op2)

elif char == '/':
    division(op1, op2)

elif char == '%':
    remainder(op1, op2)

else:
    print("Invalid Operation!!")
