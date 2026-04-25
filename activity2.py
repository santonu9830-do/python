a = 10
b = 12
c = 12

print(not (a == b))
print(not (b == c))

a = "apple"
b = "banana"

if a != b:
    print("a and b are different.")

a = 1
b = 3

if (a == 1) != (b == 5):
    print("Hello")

a = int(input("Enter an integer: "))

if not (a % 2 == 0):
    print(a, "is not an even number. It is odd.")
