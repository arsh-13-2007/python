# palindrome or not
sum = 0 
n = int(input("enter number : "))
a = n  
for i in range(len(str(n))):
    rem = n % 10 
    sum = sum * 10 + rem
    n = n // 10 
    
if (a == sum ):
    print(a,"is a palindrome number")
else:
    print(a,"is not a palindrome number")

