a = input("enter number : ")
count  = 0 
counta = 0
counte = 0
counto = 0
counti = 0
countu = 0
a.lower()

for i in range(len(a)):
    if(a[i]== 'a'or  a[i]== 'e'or  a[i]== 'i'or a[i]== 'o'or a[i]== 'u'):
        count += 1
        if( a[i]== 'a'):
            counta += 1
        elif( a[i]== 'e'):
            counte += 1
        elif( a[i]== 'i'):
            counti += 1
        elif( a[i]== 'o'):
            counto += 1
        elif( a[i]== 'u'):
            countu += 1

print(count)
print( "a" ,  counta)
print("e" , counte)
print( "i",counti)
print("u",countu)
print("o",counto)



