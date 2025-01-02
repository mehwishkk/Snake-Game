from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
color_seg=['purple','orange','red']
   #to store turtle objects(3)

class Snake:                           #when object of this class gets created, init will get executed
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]



    def create_snake(self):
        for pos in STARTING_POS:
           self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
       self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):  # prints from 6 to 1 / for n in range(6,0,-1): #prints from 6 to 1

            new_x = self.segments[seg_num - 1].xcor()  # segments[1].xcor()
            new_y = self.segments[seg_num - 1].ycor()  ##segments[1].xcor()
            self.segments[seg_num].goto(new_x, new_y)  # segments[2].goto()  got to in place of segmwnts[1]
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
           self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
           self.segments[0].setheading(270)
    def right(self):
        if self.head.heading() != 180:
           self.segments[0].setheading(0)
    def left(self):
        if self.head.heading() != 0:
           self.segments[0].setheading(180)
