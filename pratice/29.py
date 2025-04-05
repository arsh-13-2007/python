# armstrong number 
num = int(input("enter number : "))
sum = 0   
a = num 
b = a 
for i in range(len(str(num))):
    rem = a % 10 
    sum = sum + rem*rem*rem
    a = a // 10

if ( sum == b ):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
