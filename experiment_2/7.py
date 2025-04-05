def convert(second):
    min = second / 60 
    hour = min / 60
    print("number of min. : ", min)
    print("number of hour : ", hour)


second = int(input("enter number of second :"))
convert(second)