from abc import ABC,abstractmethod
class father(ABC):
    @abstractmethod
    def display(self):
        pass
    
class child(father):
    def display(self):
        print("this is a child class")
class relative(father):
    def display(self):
        print("this is a father class")
        print("defining relative method")
c1=child()
c2=relative()
c2.display()