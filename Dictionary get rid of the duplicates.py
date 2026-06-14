student_data = {
    "id1": {"name": "Alice", "age": 20 , "Subject_integration": "Math , English , Science"},
    "id2": {"name": "Bob", "age": 22 , "Subject_integration": "Math , English , Science"},
    "id3": {"name": "Alice", "age": 20 , "Subject_integration": "Math , English , Science"},
    "id4": {"name": "David", "age": 23 , "Subject_integration": "Math , English , Science"},
}
result = {}
seen_keys = []

for student_id, details in student_data.items():
     unique_key = (details["name"], details["age"], details["Subject_integration"])

if unique_key not in seen_keys:
 seen_keys.append(unique_key)
result[student_id] = details

for k, v in result.items():
   print(k, ":" , v)