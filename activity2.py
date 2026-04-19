cost_price = float(input("Enter the Cost Price: "))
selling_price = float(input("Enter the Selling Price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("Total profit = {0}".format(profit))
    
    