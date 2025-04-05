a = int(input("enter year : "))
if (a % 4 == 0 and (a % 400 == 0 or a % 100 != 0 )):
    print("leap year")
else:
    print("not leap year")