# Program to reverse a number

def reverse_number(num):
 
    reverse_number = 0
    original_number = num

    while num > 0:
        reminder = num % 10
        reverse_number = (reverse_number * 10) + reminder
        num = num // 10

    print(f"\nOriginal Number is: {original_number}")
    print(f"Reversed Number is: {reverse_number}")

    return reverse_number

given_number = int(input("\nEnter a number: "))
result = reverse_number(given_number)
