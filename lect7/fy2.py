def sum(n):
    sum = 0 
    for i in range(n):
        sum = sum + i**3
    return sum

n = int(input("enter number :"))
s = sum(n)
print("sum of cube of  all positive number smaller then" ,n, ":",s)