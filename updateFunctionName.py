# Program to assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

# call using original name
display_student("Soumen", 77)

# assigning new name
show_Student = display_student

# call using new name
show_Student("Soumen", 77)
