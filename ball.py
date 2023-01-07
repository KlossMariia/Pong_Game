from turtle import Turtle

# this class is responsible for creating the ball
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move

    def speed_increase(self):
        if self.move_speed != 0:
            self.move_speed -= 0.01

    def speed_reset(self):
        self.speed("slow")
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def restart(self):
        self.goto(0, 0)


