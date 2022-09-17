from turtle import Turtle
import random
#
class Obstacle(Turtle):
    #
    def __init__(self, position, min_speed, max_speed):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.setposition(position)
        self.setheading(180)
        self.move_step = random.randint(min_speed, max_speed)
        self.radius = 12
    #
    def move(self):
        self.forward(self.move_step)
    #
    def is_position_left_out_of_bounds(self):
        x_position = self.xcor()
        if x_position < -300:
            self.move_step = - self.move_step
            return True
        #
        return False
    #
    def is_position_right_out_of_bounds(self):
        x_position = self.xcor()
        if x_position > 300:
            self.move_step = - self.move_step
            return True
        #
        return False