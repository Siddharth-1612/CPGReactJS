class notification:
    def send(self):
        print("A notification has been sent to the user")
class email_notification:
    def send(self):
        print("An email notification has been sent to the user")
class sms_notification:
    def send(self):
        print("A SMS notification has been sent to the user")
obj_1=email_notification()
obj_2=sms_notification()
obj_1.send()
obj_2.send()
