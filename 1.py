f= open("file.txt")
c =f.read()
if ( "upes" in c):
    print("found")
else:
    print("not found")
f.close()