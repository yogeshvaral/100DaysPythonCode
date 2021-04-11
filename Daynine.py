## Dictionaries
# import only system from os
from os import system, name
from time import sleep


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    # print out some text


# print('hello geeks\n' * 10)

# sleep for 2 seconds after printing Output
# sleep(2)

# now call function we defined above
# clear();

bidder_list = {}
increment = True
while increment:
    name = input("Please enter your name")
    ammount = input("Please enter your bidding ammount:")
    bidder_list[name] = ammount
    print(bidder_list)
    continue1 = input("Are there any other bidders ? Type 'yes' or 'no'")
    if continue1 == 'no':
        increment = False



max_name =""
max_ammount = 0
for key in bidder_list:
    if max_ammount < int(bidder_list[key]):
        max_ammount = int(bidder_list[key])
        max_name = name

print(f" Mr {max_name} has won the bid with bidding amount {max_ammount}")


