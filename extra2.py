# Student Report Card with Correct Percentage Formula

print("===== STUDENT REPORT CARD =====")

# Student details
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

# Marks input (each subject out of 100)
marks = {
    "Math": float(input("Enter marks in Math: ")),
    "Science": float(input("Enter marks in Science: ")),
    "English": float(input("Enter marks in English: ")),
    "Geography": float(input("Enter marks in Geography: ")),
    "History": float(input("Enter marks in History: ")),
    "Computer": float(input("Enter marks in Computer: "))
}

# Total and percentage (OUT OF 600)
total = sum(marks.values())
percentage = (total / 600) * 100

# Grade calculation
if percentage >= 90:
    grade = "A1"
elif percentage >= 80:
    grade = "A2"
elif percentage >= 70:
    grade = "B1"
elif percentage >= 60:
    grade = "B2"
else:
    grade = "C"

# Subject comparison
highest_subject = max(marks, key=marks.get)
lowest_subject = min(marks, key=marks.get)

# Display report
print("\n===== REPORT CARD =====")
print("Name:", name)
print("Roll No:", roll)

print("\nMarks:")
for subject, mark in marks.items():
    print(subject, ":", mark)

print("\nTotal Marks:", total, "/ 600")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

print("\n===== PERFORMANCE ANALYSIS =====")
print("Best Subject:", highest_subject, "(", marks[highest_subject], ")")
print("Weakest Subject:", lowest_subject, "(", marks[lowest_subject], ")")

# Comparison with average marks (out of 100)
average_marks = total / 6
print("\nSubject-wise Comparison with Average:")
for subject, mark in marks.items():
    if mark > average_marks:
        print(subject, "is above average")
    elif mark < average_marks:
        print(subject, "is below average")
    else:
        print(subject, "is equal to average")