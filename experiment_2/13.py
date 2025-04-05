def character_in_string(character, string):
    return character in string
char = 'a'
text = 'Hello, world!'
if character_in_string(char, text):
    print(f"The character '{char}' is present in the string.")
else:
    print(f"The character '{char}' is not present in the string.")
