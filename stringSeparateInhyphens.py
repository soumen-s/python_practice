# Split a string on hyphens and enter them in separated lines

string = input("\nEnter a hyphen-separated string: ")
print("\nOriginal String is:", string)

# Spliting the string
sub_strings = string.split("-")

print("\nDisplaying each substring :")
for sub in sub_strings:
    print(sub)
