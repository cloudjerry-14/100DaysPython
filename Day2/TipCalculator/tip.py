print(" *********** Hi , Welcome to Tip Calculator ************")

total_bill=float(input("Please enter your total bill\n"))
print(f"Your total bill is {total_bill}")

tip_percentage=int(input("Please enter the tip percentage \n"))
print(f"You are giving a tip of {tip_percentage}")

total_people=int(input("Please enter no of people splitting the bill\n"))
print(f"The bill will split between {total_people} people\n")

final_bill=round(((total_bill + (total_bill*tip_percentage)/100)/total_people),2)
print(f"Each person will have to pay {final_bill}")