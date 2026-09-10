class Car:
    @staticmethod
    def start():
        print("The car has started...")
    @staticmethod
    def stop():
        print("The car has stopped...")
class Toyotacar(Car):
    def __init__(self,brand):
        self.brand = brand
class Fortuner(Car):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
car1.stop()