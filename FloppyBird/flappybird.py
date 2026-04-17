from turtle import Turtle

STARTING_POSITION = (-240, -40)
MOVE_DISTANCE = 10


class Bird(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.back(MOVE_DISTANCE)



