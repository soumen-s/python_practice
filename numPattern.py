"""
Program to print the following pattern ->

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

m = 5  #no. of lines in the pattern
n = 5  #no. of digits coming

for i in range(0,m+1):
    for j in range(n-i,0,-1):
        
        print(j,end=' ')
        
    print()
    