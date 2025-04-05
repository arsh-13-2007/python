# swap = two number :  
def swap(a, b ):
 a = a+ b 
 b = a- b 
 a = a - b
 print("first number : ",a)
 print("second number : ",b)
 
a = int(input("enter first  number : "))
b = int(input("enter second number :"))
swap(a, b )
