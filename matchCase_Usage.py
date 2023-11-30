#program to use match-case, just like switch-case in C

take = int(input("Enter any number: "))

match take:     #here we don't need to use break statement

    case 1:
        print("Case is 1")

    case 2:
        print("Case is 2")

    case 3:
        print("Case is 3")

    case _ if take >= 500:  #here we can also add conditional statements
        print("Case is above 500")    

    case _: #default
        print("Case is ",take," (default case)")    
