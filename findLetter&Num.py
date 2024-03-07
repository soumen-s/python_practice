# Program that accepts a sentence and calculate the number of letters and digits.

s = input("Enter a string: ")
d = {"DIGITS": 0, "LETTERS": 0}  # creating dictionary to initialize values

for c in s:
    if c.isdigit():        # checking whether the element is digit or letter
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass  # skip..

print("No. of Letters: ", d["LETTERS"])
print("No. of Digits: ", d["DIGITS"])
