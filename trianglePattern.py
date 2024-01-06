# Program for printing triangle pattern

def triangle(n):
	
	for i in range(0, n):
	
		for j in range(0, i+1):  #values changing acc. to outer loop
			print("* ",end="")

		print("\r")  #to ensure that each row of the pyramid is printed on the same line


n = int(input("\nEnter the number of rows for the triangle: "))

triangle(n)