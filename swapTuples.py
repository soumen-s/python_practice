# Program to swap 2 tuples

tuple1_input = input("Enter values for tuple1 (comma-separated): ")
tuple1 = tuple(map(int, tuple1_input.split(',')))


tuple2_input = input("Enter values for tuple2 (comma-separated): ")
tuple2 = tuple(map(int, tuple2_input.split(',')))

# Swapping of tuples
tuple1, tuple2 = tuple2, tuple1


print("Swapped tuple1:", tuple1)
print("Swapped tuple2:", tuple2)
