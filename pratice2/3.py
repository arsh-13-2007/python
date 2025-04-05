n1 = int(input("enter number of ingredients in pantry :"))
n2 = int(input("enter number of ingredients you want in recipe :"))
inpantry = set()
inrecipe = set()
for i in range(n1):
    inpantry.add(input("enter ingredients in pantry : "))
for i in range(n2):
    inrecipe.add(input("enter ingredients in recipe : "))
print(inpantry.difference(inrecipe))

   