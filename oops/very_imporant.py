class student:
    def __init__(self, name, sapid , phy, chem , maths ):
        self.name = name
        self.sapid = sapid
        self.phy = phy
        self.chem = chem
        self.maths = maths
    def display(self):
        print(f"Name: {self.name}, sap_id : {self.sapid}, phy:{self.phy}, maths:{self.maths},chem:{self.chem}")
    def average(self):
        return (self.phy + self.chem + self.maths)/3
    
def total(s):
    avage = 0 
    for i in s:
        avage += i.average()
    return avage/len(s)
        
        
s = []
n = int(input("enter number : "))
for i in range(n):
    name  = input("enter name:")
    sapid = input("enter sap id:")
    phy = int(input("enter phy marks:"))
    chem = int(input("enter chem marks:"))
    maths = int(input("enter maths marks:"))
    students = student(name, sapid, phy, chem, maths)
    s.append(students)

total_percentage =total(s)
print(f"average percentage is of class :  {total_percentage}")
