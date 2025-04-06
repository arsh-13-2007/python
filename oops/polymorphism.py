class complex: 
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def show_number(self):
        print(f"{self.real}i  + {self.imag}j")
    def add( self , num2 ):
        return complex(self.real + num2.real, self.imag + num2.imag)
num1 = complex(2, 4) 
num1.show_number() 

num2 = complex(4, 2)
num2.show_number()
num3 = num1.add(num2)
num3.show_number()

