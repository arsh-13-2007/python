class emp:
    def __init__(self , role , salary , department ):
        self.role = role
        self.salary = salary
        self.department = department
    def showdetail(self):
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
class engineer(emp):
    def __init__(self, name , age , role , salary , department ):
        self.name = name
        self.age = age
        super().__init__(role , salary , department )
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
e1 = engineer("Arsh" ,18, "HR" , "500000" ,"tech" )
e1.show()
