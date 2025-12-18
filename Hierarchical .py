class person:
    def __init__(self,name):
        self.name=name
class Employee1(person):
    def __init__(self,name,salary,dept):
        person.__init__(self,name)
        self.salary=salary
        self.dept=dept
    def work(self):
        print(f"{self.name} working in {self.dept} with salary {self.salary} rupees per month")
class Employee2(person):
    def __init__(self,name,salary,dept):
        person.__init__(self,name)
        self.salary=salary
        self.dept=dept
    def work(self):
        print(f"{self.name} working in {self.dept} with salary {self.salary} rupees per month")
E1=Employee1("Thanushree",24000,"CSE")
E1.work()
E2=Employee2("tharika",56000,"ML")
E2.work()