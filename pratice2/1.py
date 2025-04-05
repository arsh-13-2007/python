n = int(input("number of elements in set : "))
sold_items  = set()
for i in range(n):
    sold_items.add(input("enter elements in set : "))
print("unique product are : ")
print(sold_items)