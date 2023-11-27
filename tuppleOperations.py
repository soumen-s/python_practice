tupl = (11,13,15,13,16,21,"Soumen",True,22,13) #tupple formation 
                                               #(dupplicate element acceptable)

#tupl[3] = 17 #it will give an error as tupple is unchangeable (immutable)

print(tupl.count(13)) #count the number of elements in the tupple

print(tupl.index(13)) #it will print index(for multiple same element
                      #the indexing will applicable for the first one)

print(type(tupl)) 

tupl1 = tupl[3:7] #slicing       
print(tupl1)

print("Lenth is:",len(tupl))

#indirect way to make changes in tupple
tupl2 = ["Soumen","Mridu","Sneho","Rajid","Adrima","Animesh"] 
print("Previous - ",tupl2) 
temp_list = list(tupl2)      #converting into list       
temp_list[2] = "Sourav"  #changing
temp_list.pop(4)   #removing
tupl2 = tuple(temp_list)  #converting into tupple
print("Now - ",tupl2)