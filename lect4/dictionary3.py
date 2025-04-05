# methods of dictionary 
info =  {
    
    # "name" : "arsh ", 
    "age" : 25, 
    # "avg. marks" : 96.896,
    "grade" : "A",
    "lanugage" : ["c" , "html"],
    "address" : ("bilaspur","haryana" ),
    
}
# methods of dictionary
print(info.keys()) # print keys of dictionary
print(info.values()) # print values of dictionary
print(info.items()) # print items of dictionary
print(info.update({"name": "arsh"}))
print(info.get("grade"))
del info["lanugage"]
print(info) # print dictionary
a = list(info.items())
print(a) # print items of dictionary in list format
print(a[2:4])
print(a[0])


