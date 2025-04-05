n=int(input("enter number of elements in tuple :"))
tup = ()
for i in range(n):
   tup = tup + (int(input("enter number : ")),)
sum =  0 
for i in range(len(tup)):
   sum = sum + tup[i]
print( "sum of all value of tuple : ",sum)
print( "averge of all value of tuple : ", sum // n )   
   
