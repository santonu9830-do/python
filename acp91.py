import math

angle = float(input("Enter angle in degrees: "))

sin_value = math.sin(math.radians(angle))
cos_value = math.cos(math.radians(angle))
tan_value = math.tan(math.radians(angle))

print("sin =", sin_value)
print("cos =", cos_value)
print("tan =", tan_value)