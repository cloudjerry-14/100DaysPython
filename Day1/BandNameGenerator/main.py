import time
print("Hello, Welcome to Band Name Genrator app")

city_name=input("Please enter your city to begin \n")
print("Your city name is :", city_name)

pet_name=input("Please enter you pet name \n")
print("Your pet name is :", pet_name )


print("=============Your Band Name is genrating =====================")

# This will stop the execution for 3 seconds 
time.sleep(3)

# concatenating the strings
band_name=city_name + " " + pet_name

# printing Band Name
print("Your Band Name is : ", band_name)
