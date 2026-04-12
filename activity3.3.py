text = str(input("Enter a string: "))

print("The first letter of string is:", text[0])
print("The last letter of string is:", text[-1])
print("The length of string is:", len(text))
print("The sliced string:", text[1:3])
print("The sliced string with step value 2:", text[::2])
print("the uppercase of string is:", text.upper())
print("the lowercase of string is:", text.lower())


# Reverse String using step value -1
revText = text[::-1]

print("Reverse of given string is:")
print(revText)