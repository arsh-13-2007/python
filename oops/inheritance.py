# single inheritance 

class car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class toyota(car):
    def __init__(self ,name ):
        self.name = name
arsh = toyota("creta")
print(arsh.name)



