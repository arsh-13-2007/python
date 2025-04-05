l = []
for i in range(10):
    l.append(int(input("enter elements in list :")))
odd_list = []
even_list = []
for i in l:
    if ( i % 2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)
print("even list :", even_list)
print("odd list :", odd_list)