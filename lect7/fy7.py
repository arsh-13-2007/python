numbers =list(map(int,input("enter the numbers:").split()))

full_list = list(range(1, 11))

missing_numbers = [number for number in full_list if number not in numbers]
print("Missing numbers:", missing_numbers)
