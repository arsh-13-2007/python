input_string = "ABaBCbGc"
count_dict = {}
for char in input_string:
    char_upper = char.upper() 
    if char_upper.isalpha():     
        count_dict[char_upper] = count_dict.get(char_upper, 0) + 1
for char, count in count_dict.items():
    print(f"{count}{char}")