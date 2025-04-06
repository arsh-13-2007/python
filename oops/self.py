class emp: # class   # class attribute is same for all 
   
    age = 18
    study = "at upes"
    def greeting(self):  #wihout self we not call self 
        print(f"Hello, my name is {self.name} and I am {self.age}")
    @staticmethod #if we not want to use self keyword then we use static method 
    def system():
        print("good morning")

arsh= emp()
arsh.name = "arsh"  # instance attribute have high perference  
arsh.age = 19 
arsh.greeting() # prints: Hello, my name is emp.__main__.arsh and
arsh.system()    # in this we use static method 
