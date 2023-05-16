from turtle import Turtle
import random

COLOR = ["red","orange","yellow","green","blue","purple"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANE = 5

class Car(Turtle):

	def __init__(self):
		super().__init__()
		self.car_list = []


	def create_car(self):
		random_chance = random.randint(1,6)
		if random_chance == 1:
			new_car = Turtle('square')
			new_car.shapesize(stretch_wid=1,stretch_len=2)
			new_car.penup()
			new_car.color(random.choice(COLOR))
			
			random_y = random.randint(-230,230)
			new_car.goto(300,random_y)
			self.car_list.append(new_car)
		

	def move_cars(self):
		for car in self.car_list:
			car.backward(STARTING_MOVE_DISTANE)


