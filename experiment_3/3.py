def check(a,b):
    if ( a> b ):
        print("a is greater than b ")
    elif ( a < b ):
        print("b is greater than a")
    else:
        print("a is equal to b")
a = int(input("enter first number : "))
b = int(input("enter second number : "))
check(a,b)