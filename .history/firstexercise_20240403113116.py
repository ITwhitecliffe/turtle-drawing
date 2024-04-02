# from which file import which class
from turtle import Turtle, Screen

sir = Turtle()
sir.color("#86469C")
sir.shape("turtle")


def drawSquare():
    sir.forward(200)
    sir.left(90)
    sir.forward(200)
    sir.left(90)
    sir.forward(200)
    sir.left(90)
    sir.forward(200)


drawSquare()

screen = Screen()
print(screen.canvheight)
screen.exitonclick()
