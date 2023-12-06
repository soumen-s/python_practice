# Program to use Fibonacci using recursion

def fibo(n):
	if n==1 or n==2:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

x = int(input("\nEnter the position to get nth Fibonacci number: "))
print(f"The {x} th Fibonacci number is:",fibo(x))		

