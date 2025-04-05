n = int(input("enter number : "))
a = 3 
b = 5 
sum = 0
for i  in range(n):
    sum = a + b
    a = b 
    b = sum
print(sum)    