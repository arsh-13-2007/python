def check(a,b,c):
    if ( a > b ):
        if ( a >  c):
            print("a is greater")
        else:
            print("c is greater")
    else:
        if ( b > c):
            print("b is greater")
        else:
            print("c is greater")
            
a = int(input ("enter first number :"))
b = int(input ("enter second number :"))
c = int(input ("enter third number :"))
check(a,b,c)