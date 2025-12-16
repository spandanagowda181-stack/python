class Dog():
    sound="bark"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(f"{self.name} is eating")
d=Dog("puppy",12)
print(d.sound)
d.eat()