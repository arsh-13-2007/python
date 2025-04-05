with open("file.txt") as f:
    r=f.read()
new= r.replace("here" ,"####")
with open("file.txt", "w") as f:
    f.write(new)
        


