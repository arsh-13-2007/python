class number:
    def __init__(self, x , y ):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x},{self.y}) ")
    def __add__(self , two):
        return number(self.x + two.x , self.y + two.y)
one = number(10 , 20 )
one.show()
two = number(12 , 15 )
two.show()
three = one + two
three.show()