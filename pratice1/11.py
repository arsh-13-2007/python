n1 = int(input("enter number of elements in set 1  :  "))
n2 = int(input("enter number of elements in set 2 :  "))
s1 = set()
for i in range(n1 ):
    s1.add(input("enter elemetns in set 1 : "))
s2 = set()
for i in range(n2 ):
    s2.add(input("enter elements in set 2  : "))
  
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))


