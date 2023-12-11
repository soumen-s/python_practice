#program to find if a number is strong number or not
# 145 = 1! + 4! + 5!
def fact(x):
    if x==0:
        return 1
    else: 
        return x*fact(x-1)

def strong(n):
    store = 0
    while(n!=0):
        rem = int(n%10)
        n = int(n/10)
        store += fact(rem)

    return store
    
n = int(input("Enter the number:"))
a = strong(n)
if n == a:
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")      