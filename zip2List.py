# program to concatenate two lists index-wise using zip() function.

list1 = ["M", "na", "i", "Sou"] 

list2 = ["y", "me", "s", "men"]

list3 = [i + j for i, j in zip(list1, list2)]  
# zip sunc. takes 2 or more iterables list, dict or string, aggregates them in a tuple, and returns it.

print(list3)