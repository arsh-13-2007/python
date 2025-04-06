class student:
    def __init__(self, name,phy, maths , chem):
        self.name = name
        self.phy = phy
        self.maths = maths
        self.chem = chem
    def sum(self):
        return self.phy + self.maths + self.chem

s1 = student("arsh" ,97, 96, 95 )
avg =s1.sum()/ 3 
print(avg)


        