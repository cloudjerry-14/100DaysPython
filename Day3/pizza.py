print("Welcome to PizzaPy!")
print("-----------Menu------------\n1. Small Pizza : 15$\n2. Medium Pizza : 20$\n3. Large Pizza : 25$\n4. Topings Pepperoni : 2$\n5. Extra cheese : 1$\n -----------------------------")

bill=0

size=input("Please enter the pizza size you want - Small, Medium, Large\n")

if size=="Small":
    bill+=15
elif size=="Medium":
    bill+=20   
else:
    bill+=25

topings=input("Do you want me to add pepperoni Y or N\n")
if topings=="Y":
    bill+=2

extra_cheese=input("Do you need extra cheese Y or N\n")
if extra_cheese=="Y":
    bill+=1

print(f"Your final bill is {bill}$")