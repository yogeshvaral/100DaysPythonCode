# String manipulations
print("Hello World")
score = 0
height = 1.0
isWinning = True

print(f"your score is {score},your height is {height},you are winnig is {isWinning}")

# life in weeks exercise
age = input("what is your current age ")
age_remaining = 90 - int(age)
days_remaining = age_remaining * 365
weeks_remaining = age_remaining * 52
months_remaining = age_remaining * 12

print(f"you have {days_remaining} days,{weeks_remaining} weeks and {months_remaining} left")

## Project -  Tip Calculator

bill = input("Enter total bill")
tip_percentage = input("what is percentage of tip you would like to give")
people = input("How many people to split bill")

tip_ammount = float(bill) * (float(tip_percentage) / 100)
total_ammount = float(bill) + tip_ammount

ammount_per_person = round(total_ammount / int(people), 2)
print(f"tip ammout is {tip_ammount},total bill is {total_ammount},per persont ammount is {ammount_per_person}")
final_ammont = "{:.2f}".format(total_ammount / int(people))
print("final ammunt is "+final_ammont)
