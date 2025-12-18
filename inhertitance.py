class Animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        print(f"animal name: {self.name}")
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def eat(self):
        print(f"{self.name} is eating")
    def sound(self):
        print(f"{self.name} bark")
class cat(Animal):
    
    def sound(self):
        print(f"{self.name} meow")
d=Dog("puppy")
d.info()
d.sound()
d.eat()
c=cat("chintu")
c.info()
c.sound()
c.eat()