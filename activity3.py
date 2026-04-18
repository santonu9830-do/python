print("Enter Marks obtained in 5 subjects")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
history = int(input("History: "))
geography = int(input("Geography: "))

sum = math+science+english+history+geography
print("Total Marks obtained is", sum)
perc = (sum/500)*100
print(end="Percentage Mark =  ")
print(perc, "%")
