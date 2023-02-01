import logging
import random

from turtle import Turtle, Screen


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

logger.info("Prompting user for number of turtles")
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
logger.info(f"User prompt: {user_bet}")

# configurations
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -70
all_turtles = []

logger.info("Setting up turtles")
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_position)
    all_turtles.append(turtle)
    y_position += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                logger.info(f"You've won! The {winning_color} turtle is the winner!")
            else:
                logger.info(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.listen()

screen.exitonclick()
