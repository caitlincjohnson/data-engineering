from turtle import Turtle, Screen


def main():
    """Main script."""

    tim = Turtle()

    tim.shape("turtle")
    tim.color("green")

    for i in range(3, 11):
        for _ in range(i):
            angle = 360 / i
            tim.forward(30)
            tim.right(angle)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
