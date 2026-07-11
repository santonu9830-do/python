class Employee:
    def __init__(self):
        self.__salary = 25000

    def __salaryMessage(self):
        print("Salary Information")

    def displaySalary(self):
        self.__salaryMessage()
        print("Salary:", self.__salary)


employee = Employee()
employee.displaySalary()
