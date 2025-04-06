  # super is very useful 

class car:
    def __init__( self , type ):
        self.type = type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class toyota(car):
    def __init__(self ,name  , type):
        self.name = name  
        super().__init__(type)  # this is way to use super () method 
        super().start()
car1 = toyota("fortuner", "petrol")
print(car1.type)