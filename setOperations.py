# set creation and applying some methods on it
store = {11,13,13,13,15,"Soumen",16,False,21.2,22} 
                       #set formation
                       #it is unodered and dupplicate elements unacceptable

'''if there we also enter duplicate elements, that will not show while printing
                 curly braces are not mandatory'''

print(store) # the output might be different as in set, there is no sureity
             # that how the indexing will proceed (actually indexing doesnot work)

# print(store[0]) # give error as indexing doesnot work in set    

create = set() #creating Empty set
print(type(create))      

#---------------------------------------------
s1 = {1,2,5,7}
s2 = {3,5,8,6,9,7}

print(s1.union(s2))  #union operation performed

s1.update(s2)  # union performed and updated the set into s1 set
print(s1)  

#---------------------------------------------
s3 = {11,12,14,15}
s4 = {16,14,19,18,12,20}

print(s3.intersection(s4))  #intersection operation performed

s3.intersection_update(s4)  
print(s3)  # intersection performed and updated the set into s3 set

#---------------------------------------------
s5 = {21,22,23,25}
s6 = {24,26,27,28}

print(s5.isdisjoint(s6)) #True- because there are no similarities

s5.add(99) # to add in a set
print(s5)

s5.remove(99) # to remove from set
print(s5)