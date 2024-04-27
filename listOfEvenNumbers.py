# Program which can filter even numbers in a list by using filter function.

Lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = list(filter(lambda x: x % 2 == 0, Lists))

print("The list elements are : ",evenNumbers)
