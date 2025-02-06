from abc import ABC, abstractmethod
from typing import List
import csv

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.title = "Manager"

    def work(self):
        return f"{self.name} is the {self.title}."

    def get_salary(self):
        return self.salary

class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.title = "Developer"

    def work(self):
        return f"{self.name} is the {self.title}."

    def get_salary(self):
        return self.salary

class Intern(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.title = "Intern"

    def work(self):
        return f"{self.name} is learning and assisting."

    def get_salary(self):
        return self.salary

class Security(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.title = "Security"

    def work(self):
        return f"{self.name} is securing the assets."

    def get_salary(self):
        return self.salary

class Department:
    def __init__(self, name):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee):
        self.employees.append(employee)
        print(f"{employee.name} has been hired as {employee.title}.")

    def fire(self, employee: Employee) :
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")
    
    def get_total_salary(self):
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self):
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"{employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

    def save_to_csv(self, filename="employee_data.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Role", "Salary"])
            for employee in self.employees:
                writer.writerow([employee.name, employee.title, employee.get_salary()])
       
it_department = Department("IT")

num_employees = int(input("Enter the number of employees to add: "))
for _ in range(num_employees):
    print("\nEnter employee details:")
    name = input("Name: ")
    role = input("Role (Manager/Developer/Intern/Security): ")
    salary = float(input("Salary: "))
    
    if role.lower() == "manager":
        employee = Manager(name, salary)
    elif role.lower() == "developer":
        employee = Developer(name, salary)
    elif role.lower() == "intern":
        employee = Intern(name, salary)
    elif role.lower() == "security":
        employee = Security(name, salary)
    else:
        print("Invalid role, please try again.")
        continue
    
    it_department.hire(employee)

it_department.show_employee_details()

total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: {total_salary} Rs")

it_department.save_to_csv()
