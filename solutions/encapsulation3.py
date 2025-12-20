#1
class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary#protected attribute
e=employee('spandana',1000)
print(e.name)
print(e._salary)
#2
class manager:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(self.name)
man=manager("Arun")
man.display_name()
print(man.name)

