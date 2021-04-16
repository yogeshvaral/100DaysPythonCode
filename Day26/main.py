# List comprehension
# new_list = [new_item for item in list if test]
list = [a*2 for a in range(1, 5)]
print(list)

# Dictionary  comprehension
# new_dict = {new-kwy:new_value for (key,value) in dict.item() if test}
names = ["kaminee","yogesh","aayush","nilam"]
import random
student_dict = {student: random.randint(1,100) for student in names}
print(student_dict)
passed_stundent = {key:value for (key, value)  in student_dict.items() if value >50}
print(passed_stundent)

# Loop through dataframe
import pandas
states_df = pandas.read_csv("50_states.csv")
for(index, row) in states_df.iterrows():
    if row.state == 'Arizona':
        print(row.x, row.y)

new_state_dict = { index : row.state+","+str(row.x)+","+str(row.y) for (index,row) in states_df.iterrows()}
print(new_state_dict)

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_df)

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

user_input = input("Please enter your name")

for char in user_input.upper():
    print(f"{char}:{nato_dict.get(char)} ")

output_dict = { nato_dict[letter] for letter in user_input.upper()}
