from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        #The issue in your code is that you are using the same name, score, for both the Score class and an instance variable within the class. 
        #This causes a conflict, and when you try to call scoring.score() in your main loop, it treats score as an integer (instance variable),
        #not a method.      
        self.score=0
        with open ("high_score.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.pencolor("white")
        self.goto(0,275)
        self.hideturtle()
        self.write(arg=f"SCORE :{self.score}     HIGH_SCORE : {self.high_score}",  move=False, align="center", font=("Arial",16,"normal"))
    def scored(self):
        self.score+=1
        self.clear()
        self.write(arg=f"SCORE: {self.score}   HIGH_SCORE : {self.high_score}", move=False,align="center",font=("Arial",16,"normal"))
           
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0    
        self.scored()
        with open ("high_score.txt" , "w") as file:
            file.write(str(self.high_score))

        # self.goto(0,0)
        # self.write(arg="GAME OVER" , move=False ,align="center",font=("Arial",20,"normal"))
    
    