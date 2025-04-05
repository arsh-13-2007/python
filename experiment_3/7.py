def check(date , month , year ):
    if ( month == 1,3,5,7,8,10,12 ):
        if(date >= 1 and date <= 30 ):
            date = date+ 1
            print(date,"/",month,"/",year) 
        elif(date == 31):
            date = 1
            month = month + 1
            print(date,"/",month,"/",year)
        else:
            print("invalid date ")
    elif( month == 4,6,9,11):
        if(date >= 1 and date <= 29 ):
            date = date + 1
            print(date,"/",month,"/",year)
        elif(date == 30):
            date = 1
            month = month + 1
            print(date,"/",month,"/",year)
        else:
            print("invalid date ")
    elif(month == 2):
        if (year % 4 == 0 and year % 100 != 0 or year% 400 == 0):
            if(date >= 1 and date <= 28):
                date = date + 1 
                print(date,"/",month,"/",year)
            elif(date == 29):
                date = 1
                month = month + 1
                print(date,"/",month,"/",year)
            else:
                print("invalid date ")
        else:
            if(date >= 1 and date <= 27):
                date = date + 1
                print(date,"/",month,"/",year)
            elif(date == 28):
                date = 1
                month = month + 1
                print(date,"/",month,"/",year)
    else:
        print("invalid month ")    
date = int(input("enter data  from : "))
month = int(input("enter month ( from 1 to 12 ) :"))
year = int(input("enter year : "))
check(date, month , year  )