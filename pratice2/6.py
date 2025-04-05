n = int(input("Enter the number of elements in the set: "))
a = set()
for i in range(n):
    a.add(int(input("Enter the elements of the set: ")))

power_set = []
for k in range(2**n):
    subset = set()
    binary = bin(k)[2:].zfill(n)
    for i in range(n):
        if binary[i] == '1':
            subset.add(list(a)[i])
    power_set.append(subset)

print("Power set of the given set is: ")
for subset in power_set:
    print(subset)