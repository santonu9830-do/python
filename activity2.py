Amount =int(input("Enter the amount: "))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("The number of 100 notes is", note_1)
print("The number of 50 notes is", note_2)
print("The number of 10 notes is", note_3)