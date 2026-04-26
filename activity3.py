print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice (1 or 2): "))
if (choice == 1):
    print("You have selected Bike.")
    print("Select your bike type:")
    print("1. Sports Bike")
    print("2. Cruiser Bike")
    bike_choice = int(input("Enter your choice (1 or 2): "))
    if bike_choice == 1:
        print("You have selected Sports Bike.")
    elif bike_choice == 2:
        print("You have selected Cruiser Bike.")
if (choice == 2):
    print("You have selected Car.")
    print("Select your car type:")
    print("1. Sedan")
    print("2. Hatchback")
    car_choice = int(input("Enter your choice (1 or 2): "))

    if car_choice == 1:
        print("You have selected Sedan.")
    elif car_choice == 2:
        print("You have selected Hatchback.")
    else: 
        print("Wrong choice!!.")