# default parameters
class car():
    start="engine start"
    def __init__(self,name=None,color=None,waranty=0,speed=0):
        self.name=name
        self.color=color
        self.waranty=waranty
        self.speed=speed
    def properties(self):
        print(f"{self.color} color {self.name} car  have {self.waranty} years  waranty ,and it has the speed{self.speed}")
car1=car()
car1.properties()
car2=car("mahindra","black",3,180)
car2.properties()
