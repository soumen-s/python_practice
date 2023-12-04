# Program to get prime number in a user defined range
def prime(n):
    count = 0

    for i in range(1,n+1):
        if n%i==0:
            count += 1
    if(count == 2):       
        return 2
    else:
        return 0    

#to enter two numbers..
n,m = map(int,input("Enter the range to get prime number: ").split()) 
L = []                                     
for i in range(n,m+1):
    if(prime(i)): # while condition is true
        L.append(i)

print("The Prime numbers are: ",L)        