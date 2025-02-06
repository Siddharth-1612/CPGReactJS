from abc import ABC,abstractmethod
class userauthentication(ABC):
    @abstractmethod
    def login(self):
        print("user has logged in")
        
    @abstractmethod
    def logout(self):
        print("user has logged out")
class googleauth(userauthentication):
    def login(self):
        super().login()
        print("user has logged in through google account")
    def logout(self):
        print("user has logged out from google account")
class facebookauth(userauthentication):
    def login(self):
        print("user has logged in through facebook")
    def logout(self):
        super().logout()
        print("user has logged out from facebook")

obj_1=googleauth()
obj_2=facebookauth()
obj_1.login()
obj_2.logout()