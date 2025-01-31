class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"this car is a {self.brand} {self.model}")
c1=car('range rover','defender')
c2=car('bentley','bentayga')
c1.display_info()    
c2.display_info()    