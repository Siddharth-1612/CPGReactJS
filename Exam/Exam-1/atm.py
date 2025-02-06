def check_balance(balance):
    print(f"Your current balance is: {balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance+= amount
    else:
        print("Invalid amount!")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance-=amount
    elif amount > balance:
        print("Insufficient balance!")
    else:
        print("Invalid amount!")
    return balance

def main():
    balance = float(input("enter your balance: "))
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            break
        else:
            print("Invalid option! Try again.")

main()
