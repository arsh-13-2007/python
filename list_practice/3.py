list1 =["arsh" , "aggarwal", "percuning", "his", "from" , "upes"]
list2 = []
for i in range(len(list1)):
    str1 = str(list1[i])
    for j in range(len(str1)):
      list2.append(str1[0])
      break 
print(list2)