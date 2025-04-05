num = int(input("Enter a number: "))
def membership(number):
    sequence = (10, 20, 56, 78, 89)
    if number in sequence:
        print("Is in the sequence.")
    else:
        print("NOT in the sequence.")
membership(num)