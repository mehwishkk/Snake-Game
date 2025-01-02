from turtle import Turtle
import random

class Food(Turtle):
     def __init__(self):
         super().__init__()

         self.shape("circle")
         self.color("white")
         self.penup()
         self.shapesize(stretch_len=.5,stretch_wid=.5)
         self.refresh()
     def refresh(self):
         new_x = random.randint(-250, 250)
         new_y = random.randint(-250, 250)
         self.goto(new_x, new_y)
