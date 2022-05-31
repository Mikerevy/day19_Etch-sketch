from turtle import Turtle, Screen

# TODO: A turtle that will move on:
# w = forwards
# s = backwards
# a = counter-clockwise
# d = clockwise
# c = should clear the screen and get back tim to the start

# Create a new object tim and screen
tim = Turtle()
screen = Screen()

# Create ftions for moving our turtle:
def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(5)


# Create a ftion for clear the screen
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Set focuse on turtle screen
screen.listen()

# Moving our turtle on the screen
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)


# End our program
screen.exitonclick()
