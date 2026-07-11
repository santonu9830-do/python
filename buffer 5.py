class Student:
    def __init__(self):
        self.__marks = 85

    def __result(self):
        print("Result Generated")

    def showMarks(self):
        print("Marks:", self.__marks)


student = Student()
student.showMarks()
student._Student__result()
