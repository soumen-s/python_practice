info = {"Soumen":77, "Mridu":65, "Rajid":68, "Sourav":66} #key= Soumen & value= 77
#dictionary formation(to store two key values together)

print(info)

print(info["Mridu"])  #to get any dictionary element's value  

info["Animesh"] = 69  #to add any element in the dictionary
print(info)

info["Soumen"] = 111  #to change any elements value
print(info)

print(info.keys()) #to print all the keys

print(info.values()) #to print all the values

print("\n")
for key in info.keys(): #accessing every key   # info[key] means value
	print(f"The value correponding to the key {key} is: {info[key]}")

dic1 = {"a":65, "b":66, "c":67, "d":68}
dic2 = {"e":69, "f":70, "g":71}

dic1.update(dic2) #updating dic2 into dic1
print(dic1)

empt = {}
print(empt) #empty dictionary

dic3 = {"a":65, "b":66, "c":67, "d":68}
dic3.clear()  #clearing dictionary
print(dic3)

dic1.pop("a")  #pooping any element
print(dic1)

dic4 = {"a":65, "b":66, "c":67, "d":68}
dic4.popitem()  # last key-value will gone
print(dic4)
