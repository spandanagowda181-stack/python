class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.salary = salary    #public attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
print(emp.salary)