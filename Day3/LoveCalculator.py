print("---------Welcome to Love Calculator!----------")

person1=input("Please enter the name of first person\n").lower()
person2=input("Please enter the name of second person\n").lower()

combined_string = person1+person2
count1=0
count2=0

for i in range (len(combined_string)):
    if combined_string[i]== "l" or combined_string[i]== "o" or combined_string[i]== "v" or combined_string[i]== "e":
        count1+=1
    if combined_string[i]== "t" or combined_string[i]== "r" or combined_string[i]== "u" or combined_string[i]== "e":
        count2+=1

love_score=int(str(count2)+str(count1))
if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos !")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are all good together!")
else:
    print(f"Your score is {love_score}!")