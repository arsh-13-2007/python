n = int(input("number of value we want to add :"))
list = []
count1 = 0 
count2 = 0
count0 = 0 
count3 = 0
for i in range(n):
    list.append(int(input("enter numebr between 0 t0 3 : ")))
    if ( list[i] == 0 ):
        count0 += 1
    elif ( list[i] == 1 ):
        count1 += 1
    elif(list[i] == 2 ):
        count2 += 1
    elif(list[i] == 3 ):
        count3 += 1

print("number of 1 in list is : " , count1)
print("number of 2 in list is : " , count2)
print("number of 3 in list is : " , count3)
print("number of 0 in list is : " , count0)
