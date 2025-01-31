class student_school:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name,self.age,self.gender,end=" ")
class student_college(student_school):
    def __init__(self,name,age,gender,dept):
        super().__init__(name,age,gender)
        self.dept=dept
    def display(self):
        super().display()
        print(self.dept,end=" ")
class student_pg(student_college):
    def __init__(self,name,age,gender,dept,thesis):
        super().__init__(name,age,gender,dept)
        self.thesis=thesis
    def display(self):
        super().display()
        print(self.thesis)
student_info=student_pg("anna",18,'Female','CSE','AI&ML')
print(student_info.display())