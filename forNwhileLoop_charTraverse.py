#Program to print characters from 'a' to 'h' using for and while loop

print("\nFirst program ~")
start = ord('a') #converting into ASCII value
end = ord('h')

for i in range(start,end):
	char = chr(start)   # reconverting into character
	print(char,end = " ")
	start = start+1  # incrementing the numbers by 1

i = start
while i <= end:
	char = chr(i)
	print(char)
	i = i + 1

#for loop with else- after ending the for loop, else will print
print("\nSecond program ~")
for x in range(5):
	print(x,end = " ")

	# if(x==4): # if we add break statements in for loop, then after satisfying it
	# 	break   # the loop will end and else statement will not print

else:
	print("\nnot an i")		