from turtle import Turtle,Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)       #Turn turtle animation on/off and set delay for update drawings.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on = True
while game_is_on:
    screen.update()  #Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.2)
    snake.move()
    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food)<15:  #Return the distance from the turtle to (x,y), the given vector,
        food.refresh()                 # or the given other turtle, in turtle step units.
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()

    for seg in snake.segments:
       if seg == snake.head:
           pass
       elif snake.head.distance(seg)<15:
           game_is_on= False
           scoreboard.game_over()


screen.exitonclick()
