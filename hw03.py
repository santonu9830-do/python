# 1. Create a list of fruits
fruits = ["apple", "banana", "cherry", "dragonfruit"]

# 2. Convert the first letter of every element to capital using list comprehension
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print(f"Original list: {fruits}")
print(f"Updated list:  {capitalized_fruits}")