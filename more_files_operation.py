f = open("file.txt")
# lines = f.readlines() # it return list 
# print(lines)
# we can read in this way also 
line1 = f.readline() # it return string 
print(line1)
line2 =f.readline()
print(line2)



#                                           f. readlines() is use yo read all lines in one run ( it return list )
#                                           f.readline() is give single single line as you want



f.close()

