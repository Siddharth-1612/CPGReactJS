class Vehicle:
    def __init__(self):
        pass
    def display(self):
        print("this is a vehicle class")
        
class Car(Vehicle):
    def display(self):
        super().display()
        print("this is a car class")
class Bike(Vehicle):
    def display(self):
        super().display()
        print("this is a bike class")
class electric_car(Car):
    def display(self):
        super().display()
        print("this is an electric car")
obj_1=Car()
obj_2=Bike()
obj_3=electric_car()
obj_1.display()
obj_2.display()
obj_3.display()