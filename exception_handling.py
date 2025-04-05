# it is use to handle error 
# #                                  in this ( try)  and (except ) keyword is use   

# n = input("enter number : ")
# try:
#     y = print(int(n)*20)

   
# except ValueError:
#     print("invalid input")  # if user enter string then it will print invalid input

a= input("enter a : ")
b =input("enter b :  ")
try:
    y = int(a) / int(b)
    print(y)
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero ")  # if user enter zero then it will print
except ValueError:
    print("Error Code: invalid literal for int() with base 10: ")  # if user enter string then it will print invalid input

