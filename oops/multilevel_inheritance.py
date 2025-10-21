class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def define(self):
        print(f"Name: {self.name}, Age: {self.age}")
class emp( person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def define(self):
        super().define()
        print(f"Salary: {self.salary}")
class manager(emp): 
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def defines(self):
        print("department :",self.department)
        super().define()
    
m = manager( "arsh" , 18 , 852963,"it")
m.defines()