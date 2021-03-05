import random

print("Hello Yogesh")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["book", "laptop", "bat"]
choosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(choosen_word)
display = []
for a in range(0, len(choosen_word)):
    display += "_"
print(display)

end_of_game = False
life_count = len(stages) - 1
while not end_of_game:
    guess = input("Please enter guess letter").lower()
    print(guess)
    status = False
    for position in range(0, len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
            status = True

    print(display)
    if not status :
        print(stages[life_count])
        life_count -= 1

    if (life_count < 0):
        end_of_game = True
        print("You lost")
    elif '_' not in display:
        end_of_game = True
        print("You Win")
