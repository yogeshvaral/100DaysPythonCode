from turtle import Turtle, Screen
import random
new_turtle = Turtle()
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the colour")
print(user_bet)
colour = ["red","orange","yellow","green","blue","purple"]
x = -230
y = -100
all_turtle = []
is_race_on = False

for c in colour:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(c)
    all_turtle.append(new_turtle)
    y = y+40
    print(y)
    new_turtle.goto(x, y)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on =False
            winning_color = turtle.pencolor()
            if winning_color== user_bet:
                print(f"You won: The {winning_color} turtle is winner")
            else:
                print(f"You Lost: The {winning_color} turtle is winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()