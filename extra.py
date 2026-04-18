# Simple Interest Project
def calculate_si():
    try:
        # Taking user input
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the annual interest rate (%): "))
        t = float(input("Enter the time period (in years): "))

        # Applying the formula
        si = (p * r * t) / 100
        total_amount = p + si

        
        # Displaying the result
        print(f"\nSimple Interest: {si:.2f}")
        print(f"Total Amount (Principal + Interest): {total_amount:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")

# Run the project
calculate_si()

