from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        print("this is a concrete method")
class child(Father): 
    def display(self):
        print("this is a child")
class daughter(Father):
    def display(self):
        print("this is a daughter")
obj_1=child()
obj_2=daughter()
obj_1.display()
obj_1.show()
obj_2.display()
obj_2.show()