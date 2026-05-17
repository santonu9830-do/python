def perimeter():
    # Calculate the perimeter of a square 
    sides = int(input("Enter the number of sides of the square: "))
    perimeter = 4 * (sides)
    print("The perimeter of the square is:", perimeter)
    # Calculate the perimeter of a rectangle
    length = int(input("Enter the length of the rectangle: "))
    sides = int(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + sides)
    print("The perimeter of the rectangle is:", perimeter)
perimeter()
