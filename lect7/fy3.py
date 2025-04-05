def show(n):
    print(n)
    if (n > 0 ):
        show(n-1)
    else :
        print("done")

n = int(input("enter number :"))
show(n)