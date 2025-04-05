# search for the number x in give tuple 
a = (1, 4,9,16,25,36,49,64,81,100)
x = int(input("enter number for search : "))
i = 0 
while i <10 :
    if (a[i] == x ):
        print("number found at index ", i)
        break
    i = i + 1
print("done")
       