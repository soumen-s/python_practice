#usage of doc string

def square(n):
	'''to convert n into its square'''   # <- called doc string
	print(n**2)

square(5)
print(square.__doc__) 

# that part in the function is not a comment, it is known as doc-string. And it should declare right below the function name as a explanation purpose