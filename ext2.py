def convert_number(decimal_number):
    
    print("select optionn for binary, o for octal and h for hexadecimal")
    print("b. Binary")
    print("o. Octal")
    print("h. Hexadecimal")
    choice = input("Enter choice (b/o/h): ")
    if choice == 'b':
        print("Binary number:", bin(decimal_number))
    elif choice == 'o':
        print("Octal number:", oct(decimal_number))
    elif choice == 'h':
        print("Hexadecimal number:", hex(decimal_number))
    else:
        print("Invalid input")

decimal_number = int(input("Enter a decimal number: "))
convert_number(decimal_number)
