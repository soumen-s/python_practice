 # Program to find factors of a given number

def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)
    return factors

num = int(input("Enter a number to find factors: "))

result = find_factors(num)

print(f"The factors of {num} are: {result}")
