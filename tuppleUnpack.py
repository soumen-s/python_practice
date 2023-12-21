# Program to unpack a tuple

tup = (4, 8, 3)

print(tup)

# Unpacking the values into the variables n1, n2, and n3
n1, n2, n3 = tup
#n1, n2, n3, n4 = tup  <- not allowed

print("The addition of all the elements are:",n1 + n2 + n3)