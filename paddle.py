from turtle import Turtle

# creates paddles
class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(x=x_pos, y=y_pos)
        self.speed(0)
        self.color("white")

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
