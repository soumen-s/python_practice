#program to print a given number is armstrong number or not
#Example: 153 = 1^3 + 5^3 + 3^3

def armstrong(n):
    count = 0
    temp = n
    while n!=0:
        Rem = int(n%10) #counting to get the exponent == no. of digit in the number
        n = int(n/10)
        count += 1    

    store = 0
    while temp!=0:   #temp = 153
        rem = int(temp%10)  #rem = 3
        temp = int(temp/10)  #temp = 15
        store += pow(rem,count)  #pow(3,3)
    return store    
    
n = int(input("Enter the number:"))
hold = armstrong(n)

if(n == hold):
    print(f"{n} is a armstrong number.")
else:
    print(f"{n} is not a armstrong number.") 