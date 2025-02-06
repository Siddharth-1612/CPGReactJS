class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(f"tne name of the student: {self.name}")
        print(f"the roll no of {self.name}: {self.rollno}")
name=input("enter the name of the student ")
rollno=input(f"enter the roll number of {name}: ")
book_details=student(name,rollno)
book_details.display()