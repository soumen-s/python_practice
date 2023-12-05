# Program to use Factorial using recursion

def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

x = int(input("\nEnter the number to get Factorial: "))
print("The factorial of",x,"is:",fact(x))	