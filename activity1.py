medical_cause = input("Do you have a medical cause? (Y/N): ")

if medical_cause.upper() == 'Y':
    if input("Do you have a medical certificate? (Y/N): ").upper() == 'Y':
        print("You are allowed to give the exam.")
else:
    attendance = float(input("Enter your attendance percentage: "))
    
    if attendance > 75:
        print("You are allowed to give the exam.")
    else:
        print("You are NOT allowed to give the exam.")