def max(l):
    max = 0 
    for i in l:
        if i > max:
            max = i
    return max
def min(l):
    min = l[0]
    for i in l:
        if ( i< min):
            min = i
    return min

n = int(input("enter number of elements in list :"))
l = []
for i in range(n):
    l.append(int(input("enter number in list :")))

c = max(l)
d = min(l)
print("max number in list is : ",c)
print("min number in list is : ",d)
