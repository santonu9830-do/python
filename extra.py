def convert_temp(temp, unit):
    if unit.upper() == 'C':
        return temp * 1.8 + 32  # Celsius to Fahrenheit
    elif unit.upper() == 'F':
        return (temp - 32) / 1.8 # Fahrenheit to Celsius
    else:
        return "Invalid Unit"

# Usage
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C or F): ")
print(f"Result: {convert_temp(temp, unit)}")
