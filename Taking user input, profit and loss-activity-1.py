Cost_value = int(input("Enter your cost price:"))
Selling_value = int(input("Enter your selling price:"))

if Cost_value < Selling_value:
    print("You have earned a profit of:" , Selling_value - Cost_value)
elif Cost_value > Selling_value:
    print("You have suffered a loss of:" , Cost_value - Selling_value)
else:
    print("You have not gained or lost anything as there is no change in your cost value and selling value.")