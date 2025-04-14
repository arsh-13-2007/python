with open("file2.txt") as f:
    data = f.read()
    new=data.replace("python","java")
with open("file2.txt", "w") as f:
    f.write(new)
