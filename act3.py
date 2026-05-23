def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
print(factorial.__doc__)
print("the factorial of 5 is:",factorial(5))
print("the factorial of 0 is:",factorial(0))
print("the factorial of 10 is:",factorial(10))
print("the factorial of 20 is:",factorial(20))
print("the factorial of 100 is:",factorial(100))