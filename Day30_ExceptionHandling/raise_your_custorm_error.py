height = float(input("Height=:"))
weight = int(input("weight=:"))

if height > 3 :
    raise ValueError("Human hieght should not be greater than 3 meters")

bmi = weight / height ** 2

print(bmi)