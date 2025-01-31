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