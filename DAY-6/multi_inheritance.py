class man:
    def man_person(self):
        return "this is a man"
class woman:
    def woman_person(self):
        return "this is a woman"
    
class person(man,woman):
    def child(self):
        var='sfjgbsjl'
        l1=[1,5,3]
        print(var)
        print(l1)
        return "this is a child"
obj=person()
obj_1=obj
print(obj_1.man_person())
print(obj_1.woman_person())
print(obj_1.child())