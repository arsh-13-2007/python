
n = int(input("enter numnber of terms in series : "))
sum = 0 
a = 0 
b = 1
for i in range(n):
    print(a)
    sum = a + b 
    a = b 
    b = sum
    

