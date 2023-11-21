#Program to practice 2 types of function declarations

print("\nFunction Declaration- 1")

def average(x,y):  #here we can set value for x & y as default
    print(f"The average of {x} and {y} is:",(x+y)/2)

def anything(x,y,z):
	pass    # it indicates we can skip or avoid this function for now

a = int(input("Enter a = "))  
b = int(input("Enter b = "))  

average(a,b)

#-------------------------------------------------
print("\nFunction Declaration- 2 (Predefined)")

def avg(*numbers): #it will collect all the numbers in a tupple
	print(type(numbers)) #tupple
	total = 0
	for i in numbers:
		total = total + i

	print("Total average is: ",total/len(numbers))
		
avg(8,10,7)	#here we can add any number of data 