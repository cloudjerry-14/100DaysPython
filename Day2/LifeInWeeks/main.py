print("Hi, Welcome to the Life Remaining Calculator")
user=input("What can I call you ? \n")

your_age=int(input(f"{user} Please enter your Age: \n"))

yrs_remaining=90-your_age
months_remaining=yrs_remaining*12
weeks_remaining=yrs_remaining*52
days_remaining=yrs_remaining*7


print(f" You have {yrs_remaining} years or {months_remaining} months or {weeks_remaining} weeks or {days_remaining} days of your life, Please Enjoy it!")