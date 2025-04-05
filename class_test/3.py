date = int(input("enter date : "))
month = int(input("enter month : "))
year = int (input("enter year :"))
astrologer = date + month +year
if ( astrologer % 2 == 0 ):
    print("success")
else:
    print("fail")
