print("Welcom to Leap Year checker")

year=int(input("Enter the year!\n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap YEAR")
        else:
            print("Not a Leap YEAR")

    else:
        print("Leap YEAR")
else:
    print("Not a Leap YEAR")
