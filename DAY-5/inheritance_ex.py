class parent:
    def __init__(self):
        self.bignose='5cm'
    def display_parent(self):
        print("this is parent class")
class child(parent):
    def __init__(self):
        super().__init__()
        print("this is a constructor")
    def display_child(self):
        print("this is child class")
        
parent_obj=parent()
child_obj=child()
parent_obj.display_parent()            
child_obj.display_child()
print(child_obj.bignose)
#child_obj.display_parent()
