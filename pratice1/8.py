n = int(input("enter number : "))
list = []
for i in range(n):
    list.append(int(input("enter number : ")))
print(list)
max = 0 
for i in list:
    if ( i > max ):
        max = i
second_max = 0 
for i in list:
    if ( i >= second_max and i < max ):
        second_max = i
print("runner up :", second_max)