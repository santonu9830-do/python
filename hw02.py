# Define two sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print("-" * 40)

# Method 1: Using the symmetric_difference() method
result_method1 = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (Method 1): {result_method1}")

# Method 2: Using the ^ operator
result_method2 = set_a ^ set_b
print(f"Symmetric Difference (Method 2): {result_method2}")