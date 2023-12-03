# Program to print whether a number is prime or not (using function)  

def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1  #confirmation- whether dividing by 1 & itself or not

    return count
        
n = int(input("Enter the number: "))
hold = prime(n) #holding the number, it is divided

if(hold==2):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.") 