


n = int(input("enter number : "))
   
   
a = 0 
b = 1 
for i in range(n):
    print(a)
    sum = a + b
    a = b 
    b = sum
