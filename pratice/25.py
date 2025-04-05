count = 0 
for i in range(1,101):
    if (i % 5 == 0 or i % 7 == 0 ):
        count += 1
        print(i)
print("number that divided by 5 or 7 : ", count )
