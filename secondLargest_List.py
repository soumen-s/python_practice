# Program to find the second largest element in a list

def calc_largest(lst):
    largest_val = lst[0]
    second_largest = lst[0]

    for i in range(len(lst)):
        if lst[i] > largest_val:
            largest_val = lst[i]

    for i in range(len(lst)):
        if lst[i] > second_largest and lst[i] != largest_val:
            second_largest = lst[i]

    return second_largest

#all statements are under the function definition
print("The Second largest element is:",calc_largest([20, 30, 35, 40, 25, 10]))
