class Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Department:", self.department)

student1 = Student("Arun", 101, "Computer Science")
student2 = Student("Kiran", 102, "Artificial Intelligence")

student1.display()
print()
student2.display()
