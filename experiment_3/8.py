def grade(percentage):
    cgpa = percentage / 10
    if ( cgpa <= 10.0 and cgpa >= 9.1 ):
        print("O outstanding ")
    elif ( cgpa <= 9.0 and cgpa >= 8.1 ):
        print("A excellent ")
    elif ( cgpa <= 8.0 and cgpa >= 7.1 ):
        print("B very good ")
    elif ( cgpa <= 7.0 and cgpa >= 6.1 ):
        print("C good ")
    elif ( cgpa <= 6.0 and cgpa >= 5.1 ):
        print("D fair ")
    elif ( cgpa <= 5.0 and cgpa >= 3.5 ):
        print("E poor ")
    elif ( cgpa <= 3.4 and cgpa >= 0.0 ):
        print("F fail ")
name = input("enter name:")
sapid = int(input("enter sap_id : "))
sem = int(input("enter sem : "))
print("enter marks of given subject :")
english = int(input("enter marks of english : "))
maths = int(input("enter marks of maths : "))
python = int(input("enter marks of python : "))
chemistry = int(input("enter marks of chemistry : "))
physics = int(input("enter marks of physics : "))
# Calculating the percentage
percentage = (english + maths + python + chemistry + physics) / 5
grade(percentage)