class person:
    def __init__(self):
        pass
    def display(self):
        print("this is a person (base) class")
class employee(person):
    def display(self):
        super().display()
        print("this is a an employee which is a sub class of person")
class manager(employee):
    def display(self):
        super().display()
        print("this is a manager which is a child class of employee")
    def approve_leave(self):
        print("the leave has been approved by the manager")
obj_1=employee()
obj_2=manager()
obj_1.display()
obj_2.display()
obj_2.approve_leave()