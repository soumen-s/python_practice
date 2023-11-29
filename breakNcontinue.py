names = ["Soumen","Mridu","Sourav","Rajid","Animesh","Sneho"]

#usage of break statement
for name in names:
	if(name == "Animesh"):
		break
	print(name,end = ' ')

print("\n")
#usage of continue statement
for name in names:
	if(name == "Sourav"):
		continue
	print(name,end = ' ')
