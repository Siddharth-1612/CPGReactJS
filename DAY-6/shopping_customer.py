class Customer:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}, Phone: {self.phone}, Email: {self.email}"

class Order:
    def __init__(self, order_id, customer_id, order_status, order_date, products):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status = order_status
        self.order_date = order_date
        self.products = products 
    
    def __str__(self):
        product_list = "\n".join([f" - {product}" for product in self.products])
        return f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, Status: {self.order_status}, Date: {self.order_date}\nProducts:\n{product_list}"

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
customer =Customer(first_name, last_name, phone, email)

order_id = input("Enter order ID: ")
customer_id = input("Enter customer ID: ")
order_status = input("Enter order status: ")
order_date = input("Enter order date: ")
products = input("Enter products : ").split(",")
order = Order(order_id, customer_id, order_status, order_date, products)

transaction = Transaction()
transaction.add_transaction(customer, order)

print("\nTransaction Details:")
transaction.display_transactions()
