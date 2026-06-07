numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print ("Original list of numbers:", numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

