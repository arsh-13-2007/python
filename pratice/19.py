 # print start in equilateral triangle with for loop 
a = int(input("enter number : "))
for i in range (a):
    for j in range(a-i):
        print(" ",end="")
    for j in range (i + 1):
        print("* ",end="")
    print()    
   
