class person:
    def __init__(self,name):
        self.name=name
class job:
    def __init__(self,salary):
        self.salary=salary
class employee(person,job):
    def __init__(self,name,salary):
        person.__init__(self,name)
        job.__init__(self,salary)
    def capacity(self):
        print(f"{self.name} earns {self.salary} every month")
emp=employee("spandana",34000)
emp.capacity()