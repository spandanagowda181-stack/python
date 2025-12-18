class Emp():
    def __init__(self,name,time):
        self.name=name
        self.time=time
    def Rules(self):
        print("Rules is same for every employees")
class fun(Emp):
    def Rules(self):
        super().Rules()
        print("No rules")
d=Emp("spandana",30)

f=fun("spa",2)
f.Rules()