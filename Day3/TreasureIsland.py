print("\n----------Welcome to the Treasure Island-----------\n")

choice1=input("Please Enter a choice to move \n 1.Left  2.Right \n")
if choice1.lower()=="left":
    choice2=input("Please Enter a choice to move \n 1.Swim 2.Wait \n")
    if choice2.lower()=="wait":
        choice3=input("Please choose the door to move \n 1.Red  2.Blue 3.yellow \n")
        if choice3.lower()=="red" or choice3=="Blue":
            print("Oops wrong door, Game Over!")
        else:
            print("Celebrate! You won the Game.")
    else:
        print("Wrong choice Aligator ate you!")
else:
    print("Wrong turn, You fall into a hole")