#important set methods in python 
a = { 1, 3, 2, 5, "arsh", "aggarwal",12.4 }
b = { 1, "arsh", "hello ", 13}
# print(a.union(b))
# print(a.intersection(b))  # comman in both set 
# print(a.intersection_update(b)) #  this print only those elements which duplicate in both set 
print(a.difference(b)) # print those elements which not in b 
print(a.symmetric_difference(b)) # remove common elements :