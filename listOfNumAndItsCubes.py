# Python program to create a user defined list of tuples and creating a whole list that contains that numbers and its cube

list1 = [int(x) for x in input("\nEnter space-separated numbers: ").split()]

result = [(val, pow(val, 3)) for val in list1]


print(result)