n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    a.append(int(input("Enter element in list: ")))
print("List:", a)
max_val = 0
s_max = 0
for i in a:
    if i > max_val:
        max_val = i 
for i in a:
    if i > s_max and i < max_val:  
        s_max = i 
print("Second maximum value:", s_max)