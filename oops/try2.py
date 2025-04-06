class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        x = 3.14*3.14*self.radius
        print(x)
    def perimeter(self):
        y= 2*3.14*self.radius
        print(y)


c1 = circle(3)
c1.area()
c1.perimeter()
