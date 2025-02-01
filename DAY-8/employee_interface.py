from abc import ABC, abstractmethod
from typing import List

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

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired as {employee.title}.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")
    
    def promote(self, employee: Employee) -> None:
        if isinstance(employee, Manager):
            employee.title = "Regional Manager"
            employee.salary *= 1.3  
        elif isinstance(employee, Developer):
            employee.title = "Senior Developer"
            employee.salary *= 1.2  
        elif isinstance(employee, Intern):
            employee.title = "Full-Time Employee"
            employee.salary *= 1.5  
        print(f"{employee.name} has been promoted to {employee.title}.")
    
    def demote(self, employee: Employee) -> None:
        if isinstance(employee, Manager):
            employee.title = "Assistant Manager"
            employee.salary *= 0.8  
        elif isinstance(employee, Developer):
            employee.title = "Junior Developer"
            employee.salary *= 0.8  
        elif isinstance(employee, Intern):
            print(f"{employee.name} did not get a full-time offer and remains an intern.")
            return
        print(f"{employee.name} has been demoted to {employee.title}.")
    
    def get_total_salary(self):
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self):
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")


manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
security_staff = Security("Ram", 5000)

it_department = Department("IT")
it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(security_staff)

it_department.show_employee_details()

print("\nPromotions:")
it_department.promote(manager)
it_department.promote(developer)
it_department.promote(intern)

print("\nAfter Promotion:")
it_department.show_employee_details()

print("\nDemotions:")
it_department.demote(manager)
it_department.demote(developer)
it_department.demote(intern)

print("\nAfter Demotion:")
it_department.show_employee_details()

total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")
