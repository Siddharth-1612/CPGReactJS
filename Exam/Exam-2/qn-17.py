from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        print("file has been inserted ")
    @abstractmethod
    def update(self):
        print("file has been updated ")
    @abstractmethod
    def delete(self):
        print("file has been deleted ")
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("file has been inserted in SQLDatabase")
    def update(self):
        print("file has been updated in SQLDatabase")
    def delete(self):
        print("file has been deleted in SQLDatabase")
class NOSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("file has been inserted in NOSQLDatabase")
    def update(self):
        print("file has been updated in NOSQLDatabase")
    def delete(self):
        print("file has been deleted in MOSQLDatabase")
obj_1=SQLDatabase()
obj_2=NOSQLDatabase()
obj_1.insert()
obj_2.update()