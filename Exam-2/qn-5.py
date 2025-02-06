class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,name,stock):
        if(name==self.name and stock>=self.stock):
            print("the product is available")
        else:
            print('the product is unavailable')
name_prod=input("enter the name of the product: ")
price=float(input("enter the price of the product: "))
stock_prod=int(input("enter the requirement: "))
product_details=product(name_prod,price,stock_prod)
product_details.check_availability('apples',3)