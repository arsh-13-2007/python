#we can make nested dictionary 
nested_dict = {
    "key1": "value1",
    "key2": {
        "key3": "value3",
        "key4": "value4" ,
        },
    "key5": "value5"
    }
print(nested_dict["key2"]["key3"])  # Output: value3
