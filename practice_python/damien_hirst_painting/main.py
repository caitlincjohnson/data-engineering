import logging
import random

import colorgram
import turtle as t


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main script."""
    number_of_dots = 100

    logging.info("Set up screen variables")
    screen = t.Screen()
    screen.setup(width=500, height=500)
    screen.setworldcoordinates(
        -1, -1, screen.window_width() - 1, screen.window_height() - 1
    )

    logging.info("Set up 'turtle' variables")
    tim = t.Turtle()
    tim.hideturtle()
    t.colormode(255)
    tim.speed("fastest")
    tim.penup()

    logging.info("Extract colors from Damien Hirst's painting")
    color_objects = colorgram.extract(
        "practice_python/damien_hirst_painting/painting.jpeg", 30
    )

    list_of_rgb_colors = []
    for color_object in color_objects:
        r = color_object.rgb.r
        g = color_object.rgb.g
        b = color_object.rgb.b
        list_of_rgb_colors.append((r, g, b))

    for step in range(1, number_of_dots):
        if step % 10 < 10:
            tim.dot(20, random.choice(list_of_rgb_colors))
            tim.forward(50)

        if step % 10 == 0:
            tim.dot(20, random.choice(list_of_rgb_colors))
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

    screen.exitonclick()


if __name__ == "__main__":
    main()
