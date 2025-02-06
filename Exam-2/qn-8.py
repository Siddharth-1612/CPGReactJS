class animal:
    def speak(self):
        print("the animal makes a sound")
class dog(animal):
    def speak(self):
        print("the dog barks")
class cat(animal):
    def speak(self):
        print("the cat meows")
obj_1=dog()
obj_2=cat()
obj_1.speak()
obj_2.speak()