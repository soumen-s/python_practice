# Program to find whether a number is perfect or not
def perfect(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total += i
    return total

n = int(input("Enter the number: "))
a = perfect(n)

if n == a:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")    