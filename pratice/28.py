# prime number between 1 to 100 : 
print("prime number between 1 to 100 : ")
flag = 0 
for i in range(1,101):
    if(i == 1 ):
        continue
    elif(i == 2 or i == 3  ):
        print(i)
    else:
        for j in range(2 , i-1 ):
            if(i % j == 0):
                flag = 1
                break
            else:
                flag = 0
        if(flag == 0 ):
            print(i)
            