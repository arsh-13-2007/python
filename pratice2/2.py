n1 = int(input("enter number of sports in group A : "))
n2 = int(input("enter number of sports in group B : "))
A_group = set()
B_group = set()
for i in range(n1):
    A_group.add(input("enter sport in group A : "))
for i in range(n2):
    B_group.add(input("enter sport in group B : "))
print("common sport and hobbie between both group : ",A_group.intersection(B_group))