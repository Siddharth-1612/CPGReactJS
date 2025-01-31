# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display_info(self):
#         print(f"this car is a {self.brand} {self.model}")
# c1=car('range rover','defender')
# c2=car('bentley','bentayga')
# c1.display_info()    
# c2.display_info()    
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary  

    def set_salary(self, salary):
        self._salary = salary

    def gross_salary(self, allowances):
        
        return self._salary + allowances

    def get_salary(self):
        return self._salary

    def total_salary(self, allowances, tax, pf):
        gross = self.gross_salary(allowances)
        return gross - (tax + pf)


name = input("Enter employee name: ")
salary_1 = int(input(f"Enter the basic  salary of {name}: "))
emp = Employee(name, salary_1)

allow = int(input("Enter monthly allowances: "))
tax = int(input("Enter monthly tax deductions: "))
pf = int(input("Enter monthly PF deductions: "))

gross = emp.gross_salary(allow)
net_salary = emp.total_salary(allow, tax, pf)

print(f"Employee Name: {name}")
print(f"Gross Salary (: {gross}")
print(f"The Net Salary of {name} is: {net_salary}")
