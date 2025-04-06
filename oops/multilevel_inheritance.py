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
class fortuner(toyota):
    def __init__(self ,type):
        self.type = type
car1  = fortuner("petrol")
car1.start()