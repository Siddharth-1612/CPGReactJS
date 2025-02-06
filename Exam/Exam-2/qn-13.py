class shape:
    def area(self):
        pass
class square(shape):
    def area(self,side):
        self.side=side
        return self.side*self.side
class rectangle(shape):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        return self.length*self.breadth
side_info=float(input("enter the value of the side: "))
length_info=float(input("enter the length: "))
breadth_info=float(input("enter the breadth: "))
obj_1=square()
obj_2=rectangle()
print(obj_1.area(side_info))
print(obj_2.area(length_info,breadth_info))