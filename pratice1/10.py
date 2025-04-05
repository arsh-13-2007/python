n1 = int(input("enter number of fruits in set 1  :  "))
n2 = int(input("enter number of fruits in set 2 :  "))
s1 = set()
for i in range(n1 ):
    s1.add(input("enter fruits  in set 1 : "))
s2 = set()
for i in range(n2 ):
    s2.add(input("enter fruits in set 2  : "))
print( "common fruits : ", s1.intersection(s2))
print( "only in set 1 not in set 2 :",s1.difference(s2))
print( "differnt number of  fruits are there : ",len(s1.union(s2)))
