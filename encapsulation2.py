class Empolyee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def show_salary(self):
        print("salary: ",self.__salary)
emp=Empolyee("spandana",5000)

emp.show_salary()
