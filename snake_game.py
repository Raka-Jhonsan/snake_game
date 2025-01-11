"""
In the turtle module, the tracer() function in the Screen class is used to control the animation of turtle graphics.
Specifically, it is used to turn on or off the automatic updating of the screen after each turtle movement.

The tracer() function takes two optional arguments:

n (default=None): If specified, it controls how many turtle moves should be taken before the screen is updated. 
If n is set to a positive integer, the screen will be updated every n turtle moves. If n is set to 0, the screen
will be updated after each turtle move. If n is set to None (default), the screen will be updated after each turtle move.

delay (default=None): If specified, it controls the delay between turtle moves in milliseconds. The delay parameter 
is a positive integer or a float representing the time delay between turtle moves. If delay is set to None (default),
it means that the delay is automatically determined based on the animation speed.

"""
from turtle import Screen,Turtle
import time
#use time.sleep(1) it will delay every step by 1 sec to help know what's going on in slow motion
from snake import Snake
from food import Food
from score import Score
# import pygame
# pygame.mixer.init()
# pygame.mixer.music.load()
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake=Snake() 
food=Food()
scoring=Score()
# l

screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
# pygame.mixer.music.play(-1)
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()   

    if snake.head.distance(food)<15:
        food.refresh()
        scoring.scored()
        snake.extend()
    for segment in snake.segments[1:]:
        if segment==snake.head: 
            pass
        elif snake.head.distance(segment)<10:            
            scoring.reset()
            snake.reset_snake()
    if snake.head.xcor()<-300 or snake.head.xcor()> 290 or snake.head.ycor()<-290 or snake.head.ycor()>295 :
        scoring.reset()
        snake.reset_snake()

    
screen.exitonclick()
 






