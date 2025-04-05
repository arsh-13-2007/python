n = int(input("enter number of elements in set :  "))
word = 0 
a = set()
for i in range(n ):
    a.add(int(input("enter number in set : ")))
for  i in a:
    word +=1
print(word)