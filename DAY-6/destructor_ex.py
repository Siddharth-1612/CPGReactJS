class destructor:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
    def __del__(self):
        print(f"this object {self.name} is destroyed")

obj=destructor('abc')
del obj
