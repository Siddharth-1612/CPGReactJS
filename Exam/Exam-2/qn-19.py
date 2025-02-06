from abc import ABC,abstractmethod
class ivehicle(ABC):
    @abstractmethod
    def start_engine(self):
        print("this is the main class ivehicle")
        pass
    @abstractmethod
    def stop(self):
        pass
class car(ivehicle):
    def start_engine(self):
        super().start_engine()
        print("start the engine of the car")
    def stop(self):
        print("stop the engine of the car")
class bike(ivehicle):
    def start_engine(self):
        print("start the engine of the car")
    def stop(self):
        print("stop the engine of the bike")
class truck(ivehicle):
    def start_engine(self):
        
        print("start the engine of the truck")
    def stop(self):
        super().start_engine()
        print("stop the engine of the truck")
obj_1=car()
obj_2=bike()
obj_3=truck()
obj_1.start_engine()
obj_3.stop()