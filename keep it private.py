class MyClass:
    __privateVar = 27

    def __privMethod(self):
        print("This is a private method.")
    
    def hello(self):
        print("Private Variable:", MyClass.__privateVar)

foo = MyClass()
foo.hello()  # Accessing the private variable through a public
foo.__privMethod()  # Attempting to access the private method (will raise an AttributeError)