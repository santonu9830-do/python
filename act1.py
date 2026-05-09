string = input("Please enter your word : ")
char = input("Please enter the character you want to count : ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print("The number of times the character appears in the word is : ", count)