# dictionary 
# in dictionart we can store any data type
# we store list and tuple in dictionary 
#  dictionary are mutable 
# dictionary is key value pair 
# it is unordered 
print("hello world ")
info =  {
    # key can be string , int , float 
    "name" : "arsh ", 
    "age" : 25, 
    "avg. marks" : 96.896,
    "grad e" : "A",
    "lanugage" : ["c" , "html", "python chl rhi hei "],
    "address" : ("bilaspur","haryana" , "india"),
    13 : "arsh birthday " , 
    13.5 :"arsh" ,  
}
info["age" ] = 18 # this show that string are mutable 
print(info)
print(type(info))
print(info["name"])  # access value of key "name"
print(info["age"])  # access value of key "age"
print(info["avg. marks"])  # access value of key "avg. marks"
print(info["grade"])  # access value of key "grade"
print(info["lanugage"])  # access value of key "lanugage"
print(info["address"])  # access value of key "address"
print(info[13.5])
# we can the value of the dictionaruy 

