def compare(l1 , l2):
    for i  in l1:
        for j in l2:
            if i == j:
                print(j)


n = int(input("enter number of elements in list :"))
l1 = []
for i in range(n):
    l1.append(int(input("enter number in list 1 :")))
l2 = []
for i in range(n):
    l2.append(int(input("enter number in list 2 :")))
print(compare(l1,l2))