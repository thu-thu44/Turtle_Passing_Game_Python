from turtle import Turtle,Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time
import random


screen = Screen()
screen.bgcolor("white")
screen.title("Cross the road")
screen.setup(width=800,height=600)
screen.tracer(0)

player = Player()
car = Car()
score = ScoreBoard()

screen.listen()
screen.onkeypress(player.move,'Up')

Is_game_on = True

while Is_game_on:
	screen.update()
	time.sleep(score.speed)

	car.create_car()
	car.move_cars()

	# Detect collisin with cars
	for cars in car.car_list:
		if player.distance(cars) < 30:
			score.game_over()
			Is_game_on = False

	# Pass through the end
	if player.ycor() > 270:
		score.update_level()
		player.start_again()



screen.exitonclick()