# We will be creating a BMI calculator

print("Hi, Welcome to the BMI Calculator")

weight=int(input("Please Enter your weight:\n"))
print("Your weight is : ",weight)
height=(input("Please enter your height in meters:\n"))
print("Your height is: ",height)

bmi=(weight/float(height)**2)

if bmi < 18.5:
    print("Your BMI is :",bmi ," ----- and you're underweight, Go Gain some!")
elif bmi<=18.5 and bmi>25:
    print("Your BMI is :",bmi ," ----- and you're perfect fit, Keep up!")
else:
    print("Your BMI is :",bmi ," ----- You are Overweight, Go to the GYM!")

