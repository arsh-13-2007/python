#   with help of class we make 
class emp: # class    # we use class when any think is same for all object 
   
    age = 18
    study = "at upes"

arsh = emp() # object 
arsh.age = 19 
print(arsh.study, arsh.age)
ram = emp() # object 
print(ram.study, ram.age)  # output: at upes 18 at upes
