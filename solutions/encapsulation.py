class Empolyee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
class subEmployee(Empolyee):
    def show_salary(self):
        print("salary: ",self._salary)
emp=subEmployee("spa",45000)
print(emp.name)
emp.show_salary()
