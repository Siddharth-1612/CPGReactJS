from abc import ABC,abstractmethod
class person(ABC):
    def __init__(self,name,pan_no):
        self.name=name
        self.pan_no=pan_no
    @abstractmethod
    def display(self):
        pass
    def show_det(self):
        print(f"Name:{self.name}\n {self.name} PAN NO:{self.pan_no}")
class father(person):
    def display(self):
        print(f"Father's PAN:{self.pan_no}")
class son(person):
    def display(self):
        print(f"Sons pan_no:{self.pan_no}")
father_info=father("Pablo Escobar","hi32jjf1")
child_info=son("Escobar Jr","1234erfghu8")
father_info.display()
father_info.show_det()
child_info.display()
child_info.show_det()
