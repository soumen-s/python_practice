# Python program to find the max of two given numbers using lamda function with if-else statement.

# Lambda function is used whenever we want to create a function that will only contain simple expressions

maximum = lambda a, b: a if a > b else b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

Max = maximum(num1, num2)

print(f"The maximum of {num1} and {num2} is:", Max)