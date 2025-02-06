class ele_device:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print("this is a main class of electronic device")
class mobile_device(ele_device):
    def display(self):
        print("this is sub class of electronic device which is caleed mobile device")
class smart_phone(mobile_device):
    def __init__(self,brand):
        super().__init__(brand)
    def display(self):
        print("this is a smart phone which is a sub class of mobile device")
        print(f"its brand is {self.brand}")
brand_name=input("enter the brand of the phone:")
obj_1=smart_phone(brand_name)
obj_1.display()