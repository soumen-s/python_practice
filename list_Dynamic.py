# Dynamically creating a list

List = []  #empty list

x = int(input("Enter the size of the list: "))
for i in range(1,x+1):    #accessing the size for looping purpose
    collect = int(input(f"Enter data {i}: "))
    List.append(collect)

print("The list taken from user is:",List)    


# Updating it by incrementing its value by 10
newList = []
for i in List:   #accessing all elements
    d = i+10
    newList.append(d)

print("The updated list is:",newList)    