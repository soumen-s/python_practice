import sys

# dictionaries
dic1 = {"n1": 1, "n2": 2, "n3": 3}
dic2 = {"f1": "Mridu", "f2": "Rajid", "f3": "Sneho"}
dic3 = {1: "One", 2: "Two", 3: "Three", 4: "Four"}

# print the sizes of sample Dictionaries
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")
