class emp:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
    def display(self):
        print(f"\nname of the employee: {self.name}\nemployee id: {self.id}\nemployee department: {self.dept}")
emp_name=input("enter the name of the employee: ")
emp_id=int(input("enter the employee id: "))
emp_dept=input("enter the department of the employee: ")
employee_info=emp(emp_name,emp_id,emp_dept)
employee_info.display()