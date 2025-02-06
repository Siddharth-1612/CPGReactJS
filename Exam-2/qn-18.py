from abc import ABC,abstractmethod
class icalculator(ABC):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
class basiccalculator(icalculator):
    def __init__(self,n1,n2):
        super().__init__(n1,n2)
    def add(self):
        print(f"{self.n1}+{self.n2}={self.n1+self.n2}")
    def sub(self):
        print(f"{self.n1}-{self.n2}={self.n1-self.n2}")
    def multiply(self):
        print(f"{self.n1}*{self.n2}={self.n1*self.n2}")
    def divide(self):
        print(f"{self.n1}/{self.n2}={self.n1/self.n2}")
n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
obj_1=basiccalculator(n1,n2)
while True:
    print(" CALCULATOR")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVSION")
    print("5.EXIT")
    choice=input("enter your choice: ")
    if choice=='1':
        obj_1.add()
    elif choice=='2':
        obj_1.sub()
    elif choice=='3':
        obj_1.multiply()
    elif choice=='4':
        obj_1.divide() 
    elif choice=='5':
        print("thanks for using the calculator")
        break
    else:
        print("enter a valid choice")
         
