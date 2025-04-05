def compare(a):
    inversion = 0 
    for i in range(len(a)-1 ):
        for j in range(i ,len(a) - 1):
            if (a[i] > a[j]):
                inversion += 1
    print(inversion)



n = int(input("enter number of elements in list : "))
a = []
for i in range(n):
    a.append(int(input("enter number in list :")))
# print(a)
b = compare(a)