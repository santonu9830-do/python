start = int(input("Enter start: "))
end = int(input("Enter end: "))

squares = [i**2 for i in range(start, end + 1)]

print("Squares:", squares)
print("Even squares:", [x for x in squares if x % 2 == 0])
print("Odd squares:", [x for x in squares if x % 2 != 0])