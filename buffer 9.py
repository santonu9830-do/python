from abc import ABC, abstractmethod


class Employee(ABC):
    def display(self, name):
        print(f"Employee Name: {name}")

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        print("Developer is writing code.")


class Teacher(Employee):
    def work(self):
        print("Teacher is teaching students.")


dev = Developer()
dev.display("Alice")
dev.work()

teach = Teacher()
teach.display("Bob")
teach.work()
