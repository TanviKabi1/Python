employees = [
    ("Arun", 25000),
    ("Meera", 40000),
    ("Karthik", 32000),
    ("Divya", 45000)
]

annual_salary = list(map(lambda emp: (emp[0], emp[1] * 12), employees))
high_salary = list(filter(lambda emp: emp[1] >= 35000, employees))
bonus = list(map(lambda emp: emp[1] * 0.10, employees))

print("Employee Records:", employees)
print("Annual Salaries:", annual_salary)
print("Employees Earning 35000 or More:", high_salary)
print("Employee Bonuses:", bonus)
