import os

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"


class StudentManager:
    FILE_NAME = "students.txt"

    def add_student(self, student):
        with open(self.FILE_NAME, "a") as file:
            file.write(str(student) + "\n")
        print("Student added successfully!")

    def view_students(self):
        if not os.path.exists(self.FILE_NAME):
            print("No records found.")
            return

        with open(self.FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No student data available.")
            return

        print("\nRoll\tName\tMarks")
        print("-" * 30)
        for s in students:
            roll, name, marks = s.strip().split(",")
            print(f"{roll}\t{name}\t{marks}")

    def search_student(self, roll_no):
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                if roll == roll_no:
                    print(f"Found: Roll: {roll}, Name: {name}, Marks: {marks}")
                    return
        print("Student not found.")

    def update_student(self, roll_no):
        updated = False
        students = []

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                if roll == roll_no:
                    name = input("Enter new name: ")
                    marks = input("Enter new marks: ")
                    students.append(f"{roll},{name},{marks}\n")
                    updated = True
                else:
                    students.append(line)

        with open(self.FILE_NAME, "w") as file:
            file.writelines(students)

        if updated:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    def delete_student(self, roll_no):
        deleted = False
        students = []

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                roll, _, _ = line.strip().split(",")
                if roll != roll_no:
                    students.append(line)
                else:
                    deleted = True

        with open(self.FILE_NAME, "w") as file:
            file.writelines(students)

        if deleted:
            print("Student deleted successfully!")
        else:
            print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = input("Enter marks: ")
            student = Student(roll, name, marks)
            manager.add_student(student)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            roll = input("Enter roll number to search: ")
            manager.search_student(roll)

        elif choice == "4":
            roll = input("Enter roll number to update: ")
            manager.update_student(roll)

        elif choice == "5":
            roll = input("Enter roll number to delete: ")
            manager.delete_student(roll)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
