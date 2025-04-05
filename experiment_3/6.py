# check leap year or not 
def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year,"  given year is leap year ")
    else:
        print(year,"  given year is not leap year ")
year = int(input("enter year : "))
leap_year(year)

