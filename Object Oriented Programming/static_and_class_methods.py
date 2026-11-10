class Employee:
    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.10

    @classmethod
    def change_company(cls, name):
        cls.company = name

    def display(self):
        print("Employee:", self.name)
        print("Company:", Employee.company)
        print("Salary:", self.salary)

worker = Employee("Meera", 40000)
worker.display()
print("Bonus:", Employee.calculate_bonus(worker.salary))
Employee.change_company("Global Tech")
worker.display()
