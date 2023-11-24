# program to use different important methodes of list data structure
integers = [11,22,13,14,"Soumen",True,15.3] #list formarion


integers.append(77) #1. add the integer at the end of the list

integers.insert(3,99) #2. it will insert 99 at 3rd index in list

#integers.sort()  ## it will perform sorting if there exist only integers

#integers.sort(reverse = True) ## it would print in reverse order
#print(integers)

print(integers[2]) #3. print the integer at index 2

print(integers[0:3]) #4. it will print from 0 to index 2

print(len(integers)) #5. print the length of the integer

for i in integers: #6. traversing 'i' no. of integers using for loop
	print(i)

k=0
while k < len(integers): #7. traversing 'k' no. of integers using while loop
	print(integers[k])
	k = k+1

integers.clear() #8. To remove all elements
print(integers)

lst = [i for i in range(1,11)] #another type of list creation
print(lst)

lst1 = [i for i in range(1,11) if i%2 == 0] #also we can add conditions
print(lst1)  

m = [1000,1100,1200]  #to extend a list using another list
lst1.extend(m)
print(lst1)

h = lst + m  #to concatenate 2 lists together in a new list
print(h)
