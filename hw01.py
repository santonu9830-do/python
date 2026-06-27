test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
target_value = 1

count = 0
for value in test_dict.values():
    if value == target_value:
        count += 1

print(f"The value {target_value} appears {count} times.")
# Output: The value 1 appears 3 times.