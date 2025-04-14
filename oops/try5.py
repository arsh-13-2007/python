class student:
    def __init__(self, name, sap ,phy, chem , maths ):
        self.name = name
        self.sap = sap
        self.phy = phy
        self.chem = chem
        self.maths = maths
    def dispaly(self):
        print(f"Name: {self.name}")
        print(f"SAP: {self.sap}")
        print(f"phy:{self.phy}")
        print(f"maths:{self.maths}")
        print(f"chem:{self.chem}")
    def percentage(self):
        return ( self.phy + self.chem + self.maths)/3

s= []
for i in range(2):
    name = input("Enter your name: ")
    sap = int(input("Enter your SAP: "))
    phy = int(input("Enter your Physics marks: "))
    chem = int(input("Enter your Chemistry marks: "))
    maths = int(input("Enter your Maths marks: "))
    s1 = student(name , sap , phy , chem , maths)
    s.append(s1)
for i in s:
    x = i.percentage()
    print(f"Percentage of {i} student : {x:.2f}%")