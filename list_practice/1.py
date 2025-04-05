list1 = [ 1, 3, 2, 4, 2, 4,2 ,5]
count = 0 
n = int(input("enter number that you want to search :"))
for i in range(len(list1)):
    if ( list1[i] == n ):
        print(n, " is found at index ", i )
        count +=1
print(n , "appears",count,"times in list")

