class car:
    def move(self):
        print("this is a car")
class airplane:
    def move(self):
        print("this is an airplane")
class flyingcar(car,airplane):
    def move(self):
        print("the flying car is the combination of car and an airplane")
obj_1=flyingcar()
obj_1.move()