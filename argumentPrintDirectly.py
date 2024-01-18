# we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

def func(*args):
    for i in args:
        print(i,end = " ")

func(20, 57, 60)
func(80, 100)       # directly printing the arguments
func(11,"Soumen",33,'S',5.5,66)