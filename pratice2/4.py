
n = int(input("enter number of user in day : "))
facebook = []
for i in range(n):
    facebook.append(input("enter number : "))
inset = set(facebook)
list1 = list(inset)
for i in range(len(list1)):
    i = list1[i]
for i in range(len(facebook)):
    if (i == facebook[i]):
        i = i+ 1
for i in range(len(list1)):
    print(i)
