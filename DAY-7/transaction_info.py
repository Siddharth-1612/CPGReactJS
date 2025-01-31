import customer_info
import order_info
class Transaction: 
    def __init__(self):
        self.transactions = {}
    
    def add_transaction(self, customer, order):
        key = f"{customer.first_name} {customer.last_name}"
        if key in self.transactions:
            self.transactions[key].append(order)
        else:
            self.transactions[key] = [order]
    
    def display_transactions(self):
        for customer, orders in self.transactions.items():
            print(f"\nCustomer: {customer}")
            for order in orders:
                print(order)

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")
customer = customer_info.Customer(first_name, last_name, phone, email)

order_id = input("Enter order ID: ")
customer_id = input("Enter customer ID: ")
order_status = input("Enter order status: ")
order_date = input("Enter order date: ")
products = input("Enter products : ").split(",")
order = order_info.Order(order_id, customer_id, order_status, order_date, products)

transaction = Transaction()
transaction.add_transaction(customer, order)

print("\nTransaction Details:")
transaction.display_transactions()
