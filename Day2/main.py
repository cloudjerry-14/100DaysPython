# adding digits of a 2 digit number

two_digit_no=input("Enter 2 digit no :\n")

first_digit=int(two_digit_no[0])
second_digit=int(two_digit_no[1])

print(first_digit + second_digit)


# floor division

result=8 // 3 # This will always return a integer value
print(type(result))
print(result)

# f- strings
name="jack"
age=34
is_married=True
print(f"Hi, I am {name} {age} yrs old and I'm married : {is_married}")
