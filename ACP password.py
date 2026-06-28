import random
import string

# Define characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits

# Combine all characters
all_chars = lower + upper + numbers

# Take password length from user
length = int(input("Enter password length: "))

# Generate password
password = random.sample(all_chars, length)

# Shuffle the password
random.shuffle(password)

# Convert list into string
password = "".join(password)

print("Generated Password:", password)