from turtle import Turtle
import turtle
#
class Scoreboard(Turtle):
    #
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
    #
    def draw_final_line(self):
        line = Turtle()
        line.penup()
        line.hideturtle()
        line.setposition(-300, 200)
        line.pendown()
        line.setposition(300, 200)
    #
    def print_final_message(self, option):
        self.clear()
        self.setposition(0, 0)
        message = "You LOST!!!"
        if option:
            message = "You WON!!!"
        #
        self.write("Game Over.\n" + message, True, align="center", font=("Arial", 12))