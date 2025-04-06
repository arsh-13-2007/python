class emp:
    def __init__(self , name , age ): # this exceute always
        self.name = name
        self.age = age
    def greeting(self):
        print(f"Hello , my name is {self.name} and I am {self.age}")



a = emp("arsh" , 18 )
a.greeting()  # this will print the greeting message