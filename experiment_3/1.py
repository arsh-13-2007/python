def check(n):
    if(n%3== 0 and n % 5 == 0 ):
        print("number is divisible by 3 and 5 :", n)
    else:
        print("number is not divisible by 3 and 5", n)
    
n = int(input("enter number : "))
check(n)