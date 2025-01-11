# 
from turtle import Turtle

# class Snake:
#     def __init__(self) -> None:
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]  # Assign head to the first segment

#     def create_snake(self):
#         x_pos = 0
#         for _ in range(3):
#             self.add_Segment(x_pos)
#             x_pos += 20

#     def move(self):
#         for seg_idx in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_idx - 1].xcor()
#             new_y = self.segments[seg_idx - 1].ycor()
#             self.segments[seg_idx].goto(new_x, new_y)
#         self.head.forward(20)

#     def add_Segment(self, position):
#         turt = Turtle("square")
#         turt.color("blue")
#         turt.penup()
#         turt.setx(position) 
#         turt.sety(position)
#           # Set y-coordinate to 0 or adjust based on your requirement        
#         self.segments.append(turt)
    
#     def extend(self):
#         Last_segment=self.segments[-1].position()
#         self.add_Segment((Last_segment))


#     def right(self):
#         self.head.right(90)   
#     def left(self):
#         self.head.left(90) 
#     def down(self):
#         self.head.backward()
#     def up(self):
#         if self.head.heading!=180:
#           self.head.forward() 
from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Assign head to the first segment

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            self.add_segment(x_pos,0)
            x_pos -= 20  # Adjust the initial x-coordinate for a horizontal snake

    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, x,y ):
        turt = Turtle("square")
        turt.color("blue")
        turt.penup()
        turt.goto(x,y)
        self.segments.append(turt)

    def extend(self):
        # Use the position of the last segment to add the new one
        last_segment = self.segments[-1]
        self.add_segment(last_segment.xcor(), last_segment.ycor())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0] 

    def right(self):
        self.head.right(90)

    def left(self):
        self.head.left(90)



            