class Animal:
    def sound(self):
        print("animal sounds")
class dog(Animal):
    def sound(self):
        print("Dog bark")
class cat(Animal):
    def sound(self):
        print("cat meow")
A=Animal()
A.sound()
D=dog()
D.sound()
C=cat()
C.sound()