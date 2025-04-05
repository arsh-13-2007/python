def sum(n):
    sum = 0 
    for i in range(n+1):
        sum += i
    print(sum)    
n = int(input("Enter number : "))
sum(n)