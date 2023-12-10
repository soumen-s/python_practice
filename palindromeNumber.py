# Program to find whether a number is palindrome or not (ex: 2332,12321)
def palindrome(n): #275
    temp = n
    result = 0
    while n!=0:
        rem = int(n%10)   # 275 % 10 = 5,7,2
        n = int(n/10)     # 275/10 = 27,2,0
        result = result*10 + rem  # 0*10 + 5 = 5, 5*10 + 7 =57, 57*10 + 2 = 572
    return result
    
n = int(input("Enter the number:"))
hold = palindrome(n)

if(n == hold):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.") 