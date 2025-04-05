num=int(input("Enter a number: "))
def shift(num, shift_by):
    left = num << shift_by  
    right = num >> shift_by 
    print("Left Shift : ",left)
    print("Right Shift : ",right)
shift_by = int(input("Enter shift value: "))
shift(num, shift_by)