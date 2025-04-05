a1 = 0, b= 0 , c = 0 , d = 0 , e = 0 , f = 0 
a = []
for i in range(0,10):
    a.append(input("enter number :"))
a.sort()
print(a)
for i in range(len(a)) :
    if (a[i] =="A"):
         a1 = a1 + 1 
    elif (a[i] =="B"):
        b = b + 1
    elif (a[i] =="C"):
        c = c + 1
    elif (a[i] =="D"):
        d = d + 1 
    elif (a[i] =="E"):
        e = e + 1
    elif (a[i] =="F"):
        f = f + 1
print ("number of student of a grade : ", a1)
print ("number of student of b grade : ", b)
print ("number of student of c grade : ", c)
print ("number of student of d grade : ", d)
print ("number of student of e grade : ", e)
print ("number of student of f grade : ", f)
