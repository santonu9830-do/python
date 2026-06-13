
def palind(r):
    e = len(r) - 1
    s = 0
    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True

number = input("Enter a number: ")
if palind(number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")






















