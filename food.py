from turtle import Turtle
import random
class Food(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("Blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        randomx=random.randint(-180,180)
        randomy=random.randint(-180,180)
        self.goto(randomx,randomy)

