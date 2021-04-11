with open("my_file.txt") as file:
    content = file.read()
    print(content)


# with open("my_file.txt",mode="a") as file1:
#     file1.write("\nThis is new text")
#
# with open("my_file1.txt",mode="a") as file1:
#     file1.write("\nThis is new file1 text")

with open("./Input/Names/Invited_Names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        with open("./Input/Letters/Starting_Letter.txt") as letter_file:
            letter = letter_file.read()
            name = name.replace("\n","")
            letter = letter.replace("name", name)
            output_file_name = f"./Output/ReadyToSent/letter_for_{name}.txt"
            with open(output_file_name, mode="w") as output_file:
                output_file.write(letter)
