class Employee:
    company_name = "ABC Company"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


employee1 = Employee(101, "Rahim", 25000)
employee2 = Employee(102, "Karim", 30000)

print("Company Name:", Employee.company_name)

print("\nEmployee 1 Details:")
print("Employee ID:", employee1.emp_id)
print("Name:", employee1.name)
print("Salary:", employee1.salary)

print("\nEmployee 2 Details:")
print("Employee ID:", employee2.emp_id)
print("Name:", employee2.name)
print("Salary:", employee2.salary)
