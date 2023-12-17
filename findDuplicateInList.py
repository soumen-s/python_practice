def lst(l):
    x = []
    for a in l:
        if a not in x: # Check if the element 'a' is not already present in the list 'x'
            x.append(a)
    
    return x


print("The list without duplicate numbers are: ",lst([1, 2, 2, 3, 3, 3, 4, 5, 5]))  
