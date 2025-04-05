def union(l1, l2):
    set_l1 = set(l1)
    set_l2 = set(l2)
    union_set = set_l1.union(set_l2)
    return list(union_set) 
n = int(input("Enter number of elements in the lists: "))
l1 = []
for i in range(n):
    l1.append(int(input("Enter number in list 1: ")))
l2 = []
for i in range(n):
    l2.append(int(input("Enter number in list 2: ")))
union_elements = union(l1, l2)
print("Union of the two lists:", union_elements)