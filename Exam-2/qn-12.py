class Payment:
    def process_payment(self):
        print("the payment is being made through: ")
class CreditCardPayment(Payment):
    def process_payment(self):
        super().process_payment()
        print("Credit Card")
        print("Credit Card are being checked")
        
class PayPalPayment(Payment):
    def process_payment(self):
        super().process_payment()
        print("PayPal")
        print("verify pay pal number")
class BitcoinPayment(Payment):
    def process_payment(self):
        super().process_payment()
        print("Bitcoin")
        print("insufficient balance in wallet")
obj_1=CreditCardPayment()
obj_2=PayPalPayment()
obj_3=BitcoinPayment()
obj_1.process_payment()
obj_2.process_payment()
obj_3.process_payment()