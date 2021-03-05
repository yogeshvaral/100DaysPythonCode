number = input("Enter the number")
if(int(number)%2==0):
    print("Number is even")
else:
    print("Number is odd")


## BMI calculator 2.0
weight = input("Please enter your weight: ")
height = input("Please enter your height")

BMI = int(weight)/float(height)**2
if BMI < 18.5:
    print("Your are under weight")
elif (BMI >= 18.5) &  (BMI < 25):
    print("Your weight is Normal")
elif (BMI >= 25) & (BMI < 30):
    print("You are overweight")
elif (BMI >= 30) & (BMI < 35):
    print("You are obese")
elif BMI > 35:
    print("You are clinically obese")


## Leap year calculations

year = int(input("Please enter Year:"))

if ((year % 4 == 0) & (year % 400 == 0)) | (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year ")


##Pizza bil model

size = input("ENter the size of pizza S M L")
add_pepperoni = input("Do you want to add Pepperoni? Y/N")
extra_Cheese = input("Extra cheese")
bill=0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_Cheese == "Y":
    bill += 1
print(f"Total bill is {bill}")

