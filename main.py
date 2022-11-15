from turtlerace import TurtleRace
from obstacle import Obstacle
from turtle import Screen
from scoreboard import Scoreboard
from configuration import setup, generate_positions
import time
#
#   screen setup
#
screen = Screen()
screen.tracer(0)
screen.screensize(setup["width"], setup["height"])
#
#   set level parameters
#
difficult = screen.textinput("Crossing Game", "Type the difficult:\n- easy\n-medium\n-hard")
n_obstacles = setup["difficult"][difficult]["number"]
obstacle_min_speed = setup["difficult"][difficult]["min_speed"]
obstacle_max_speed = setup["difficult"][difficult]["max_speed"]
obstacle_positions = generate_positions(setup["min_lim"], setup["max_lim"], n_obstacles)
#  
#   Create objects game
#
turtle = TurtleRace()
scoreboard = Scoreboard()
scoreboard.draw_final_line()
obstacles = []
for i in range(len(obstacle_positions)):
    obstacle = Obstacle(obstacle_positions[i], obstacle_min_speed, obstacle_max_speed)
    obstacles.append(obstacle)
#
#   Set listeners events
#
screen.update()
screen.listen()
screen.onkey(fun=turtle.direction_north, key="w")
screen.onkey(fun=turtle.direction_south, key="s")
screen.onkey(fun=turtle.direction_west, key="a")
screen.onkey(fun=turtle.direction_east, key="d")
#
#   main loop
#
is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.02)
    turtle.move()
    #
    for obstacle in obstacles:
        obstacle.move()
        obstacle.is_position_left_out_of_bounds()
        obstacle.is_position_right_out_of_bounds()
        #
        if turtle.is_collioned_with_obstacle(obstacle):
            scoreboard.print_final_message(False)
            is_game_over = True
            break
    #
    if turtle.is_turtle_passed_all_obstacles():
        scoreboard.print_final_message(True)
        is_game_over = True
        break
#
screen.exitonclick()