from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Circle(IShape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        circle_area=3.14*radius**2
        print(f"area of the circle is:{circle_area}")
class rectangle(IShape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        rect_area=length*breadth
        print(f"area of the rectangle is:{rect_area}")
radius=float(input("enter the radius of the circle: "))
length=float(input("enter the length of the rectangle: "))
breadth=float(input("enter the breadth of the rectangle: "))
obj_1=Circle(radius)
obj_2=rectangle(length,breadth)
obj_1.calculate_area()
obj_2.calculate_area()