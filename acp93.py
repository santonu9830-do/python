age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Error! Invalid age entered.")
else:
    print("Valid age entered.")

    if age % 2 == 0:
        print("The age is Even.")
    else:
        print("The age is Odd.")