def convert_number(decimal_number):
    print("Binary number:", bin(decimal_number))
    print("Octal number:", oct(decimal_number))
    print("Hexadecimal number:", hex(decimal_number))

number = int(input("Enter a decimal number: "))
convert_number(number)
