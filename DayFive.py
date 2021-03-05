list = input("Please enter comma seperated height of students ").split(",")
totol_height = 0
count = 0
for height in list:
    count += 1
    totol_height += int(height)

average_height =  totol_height/count
print(f"avarage height = {average_height}")

## Max student score
score = input("Please enter the student scores seperated by ,").split(",")
for n in range(0, len(score)):
    score[n] = int(score[n])

print(score)
print(max(score))
print(sum(score))
max = score[0]

for n in range(1,len(score)):
    if score[n]>max:
        max = score[n]


print(max)
count = 0
for n in range(1,101):
    if(n%2==0):
        count+=n

print(count)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ltr = ""
sml = ""
nbr = ""
for n in range(0,int(nr_letters)+1):
    ltr = ltr+letters[random.randint(0,len(letters)-1)]

for n in range(0,int(nr_symbols)+1):
    sml = sml+symbols[random.randint(0,len(symbols)-1)]

for n in range(0,int(nr_numbers)+1):
    nbr = nbr+numbers[random.randint(0,len(numbers)-1)]
print(ltr+sml+nbr)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_list = [ltr, nbr, sml]
result=""
for n in range(0,len(random_list)):
    result = result+random_list[random.randint(0,len(random_list)-n)]
