country = ["brazil", "india","china","sri lanka", "russia"]
list1 = input("enter country name : ")
flag = 0 
for i in country:
    if ( i == list1):
        flag = 1 
        break
if ( flag == 0 ):
    print("country not found")
else:
    print("country found")
