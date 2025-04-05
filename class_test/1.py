def sol(n):
    fact = 1 
    for i in range(1, n+1):
        fact = fact*i
    fact1 = 1
    for i in range(1,2*n +1 ):
        fact1 = fact1*i
    permutation = (fact1 / (fact* fact ) )
    return permutation

n = int(input("enter number:"))
b = sol(n)
binary =  int( b / n+1 ) - n 
print(binary)