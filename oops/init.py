#   with help of class we make 
class emp: # class 
   
    age = 18
    study = "at upes"
    def __init__(self , name , salary , age ): #it call automaticall 
        print("system")
    def greeting(self):  #wihout self we not call self 
        print(f"Hello, my name is {self.name} and I am {self.age}")
arsh = emp() # object 
arsh.name = "arsh"
arsh.greeting()
# ram = emp() # object 
# print(ram.study, ram.age)  # output: at upes 18 at upes
