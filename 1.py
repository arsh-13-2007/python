count = 0 
with open("file.txt") as f:
    str=""
    for word in f:
        if ( len(word) > len(str)):
            str = word
print(str)
    
