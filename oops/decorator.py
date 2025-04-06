class student:
    def __init__(self, phy, linux , maths):
        
        self.phy = phy
        self.linux  = linux 
        self.maths = maths
    
    @property
    def percentage(self):
        return (self.phy + self.linux + self.maths) / 3
arsh = student(97,91,73 ) 
print(arsh.percentage)
arsh.maths = 96
print(arsh.percentage)#  percentage change automatically when we change marks with help of property decorator 
