from turtle import Turtle
#
class TurtleRace(Turtle):
    #
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setposition(0, -250)
        self.setheading(90)
    #
    def move(self):
        self.forward(4)
    #
    def direction_north(self):
        self.setheading(90)
    #
    def direction_south(self):
        self.setheading(270)
    #
    def direction_west(self):
        self.setheading(180)
    #
    def direction_east(self):
        self.setheading(0)
    #
    def is_collioned_with_obstacle(self, obstacle):
        turtle_x_position = self.xcor()
        turtle_y_position = self.ycor()
        obstacle_x_position = obstacle.xcor()
        obstacle_y_position = obstacle.ycor()
        x_part = (turtle_x_position - obstacle_x_position) ** 2
        y_part = (turtle_y_position - obstacle_y_position) ** 2
        radius = obstacle.radius ** 2
        if x_part + y_part <= radius:
            return True
        #
        return False
    #
    def is_turtle_passed_all_obstacles(self):
        turtle_y_position = self.ycor()
        if turtle_y_position > 220:
            return True
        #
        return False
    #