class student():
    branch="ISE"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def identity(self):
        print(f"{self.name} is a student of the department {self.branch}")
stud1=student("spandana",12)
stud2=student("Thanushree",13)
stud3=student("meghana",34)
stud2.branch="CSE"
print(stud1.branch)
print(stud1.name)
stud1.identity()
print(stud2.branch)
print(stud2.name)
stud2.identity()
print(stud3.branch)
print(stud3.name)
stud3.identity()