import random
number = random.randint(0, 1)
if number == 1:
    print("Heads")
else:
    print("Tails")


##Treasure Map
row1 = ['😀', '😀', '😀']
row2 = ['😀', '😀', '😀']
row3 = ['😀', '😀', '😀']

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where you want to put treasure")
horizontal = int(position[0])-1
verticle = int(position[1])-1
print(f"horizontal = {horizontal} and verticle = {verticle}")
map[horizontal][verticle] = 'X'
print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(f"{rock}\n{paper}\n{scissors}")
list = [rock, paper, scissors]
your_choise = int(input("Please enter your choise Type 0 for Rock,,1 for Paper and 2 for scissors"))
computer_choise = random.randint(0, 2)
if your_choise < 0 and your_choise > 2:
    print("Please enter the valid number between 0 and 2")
else:
    if (your_choise == 0 and computer_choise == 2) or (your_choise == 2 and computer_choise == 1) or (your_choise == 1 and computer_choise == 0):
        print(f"you choose \n {list[your_choise]}")
        print(f"computer choose \n {list[computer_choise]}")
        print("You win")
    else:
        print(f"you choose \n {list[your_choise]}")
        print(f"computer choose \n {list[computer_choise]}")
        print("your loose")


