from turtle import Turtle
import random
from snake import Snake

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        #we are able able to use these , methods because we have inherited them from Turtle super class
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        self.penup()
        self.goto(x,y)
    def refresh(self):
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        self.penup()
        self.goto(x,y)
        

        
    
