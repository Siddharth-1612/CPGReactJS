import dis
class myclass:
    # static_var=0
    def __init__(self,name):
        # myclass.static_var+=1
        # print("this is my constructor")
        print(f"the name of the constructor is {name}")
    def __init__(self,age):
        print(f"the age of the constructor is {age}")
obj_1=myclass('abc')
# obj_1=myclass()
# obj_2=myclass()
# obj_3=myclass()
# print(obj_1.static_var)
# dis.dis(myclass)
