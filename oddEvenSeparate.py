#  Program to put Even and Odd numbers in separate lists after input a number list

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers  #returning 2 outputs

input_numbers = []
size = int(input("Enter the size of the list: "))
for i in range(1,size+1):   
    collect = int(input(f"Enter data {i}: "))
    input_numbers.append(collect)
    
even_numbers, odd_numbers = separate_even_odd(input_numbers) #giving 2 o/p separately 

print("Total Input Number List:", input_numbers)
print("Even Number List:", even_numbers)
print("Odd Number List:", odd_numbers)