# Program to print multiplication table using for loop

t = int(input("\nEnter a number to get multiplication table:"))
print(f"Multiplication table of {t} is: \n")

for i in range(1,11):  # from 1 to less than 11
	print(f"{t} x {i} = {t*i}")