class bankaccount:
    def __init__(self,acc_no,holder_name,bal):
        self.acc_no=acc_no
        self.holder_name=holder_name
        self.bal=bal
    def withdraw(self,amt):
        if amt>self.bal:
            print("Sorry you have insufficient funds")
        elif amt<=0:
            print("the amount should be a positive amount")
        else:
            self.bal-=amt
            print(f"{amt} amount withdrawn,reamining balance is {self.bal}")
    def deposit(self,amt):
        if amt<=0:
            print("deposit a valid amount")
        else:
            self.bal+=amt
            print(f"{amt} id deposited\n")
            print(f"your new balance is {self.bal}")
    def get_bal(self):
        print(f"your balance is {self.bal}")
        
account_number=int(input("enter ypur account number: "))
holder_name=input("enter the name of the accoiunt holder: ")
account_balance=int(input("enter the balance: "))
account_det=bankaccount(account_number,holder_name,account_balance)
while True:
    print("\n Bank details")
    print("1.WITHDRAWAL")
    print("2.DEPOSIT")
    print("3.CHECK BALANCE")
    print("4.EXIT")
    choice=input("enter your choice: ")
    if choice=='1':
        amt=int(input("enter the amount you wish to withdraw: "))
        account_det.withdraw(amt)
    elif choice=='2':
        amt=int(input("enter the amount you wish to deposit: "))
        account_det.deposit(amt)
    elif choice=='3':
        account_det.get_bal()
    elif choice=='4':
        break
    else:
        print("enter a valid choice between 1-4")
        
                    
        