class person:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(f"{self.name} work in a campany")
class Employee(person):
    def __init__(self,salary):
        self.salary=salary
    def purpose(self):
        print(f"{self.name} working in corporate campany to get a good salary and now he is getting {self.salary} rupees")
class Manager(Employee):
    def __init__(self,depar):
        
        self.depar=depar
    def department(self):
        print(f"{self.name} manages {self.depar} department")

e=Employee("spandana",12000)
e.purpose()
M=Manager("spandana",12000,"accounts")
M.department()