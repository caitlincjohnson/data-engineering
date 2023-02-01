import logging

from turtle import Turtle, Screen


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


turtle = Turtle()
screen = Screen()


def move_forward():
    logger.info("Moving forward")
    turtle.forward(distance=10)


def move_backwards():
    logger.info("Moving backwards")
    turtle.backward(distance=10)


def move_counter_clockwise():
    logger.info("Turning left")
    turtle.left(angle=10)


def move_clockwise():
    logger.info("Turning right")
    turtle.right(angle=10)


def clear():
    logger.info("Clearing screen")
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()

# higher order functions
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
