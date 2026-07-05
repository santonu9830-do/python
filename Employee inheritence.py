class employee( object ):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

class manager(employee):
    def __init__(self, name, age, salary, post):
        self.salary = salary
        self.post = post

        employee.__init__(self, name, age, salary)

a = manager("Santonu", 25, 25000, "Manager")
a.display()