from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(x=0, y=163)
        self.write(f" score= {self.score}",align="Center",font=('Arial',20,'normal'))
        self.hideturtle()
    def game_over(self):
        self.goto(0,0)
        self.write(f" GAME OVER ", align="Center", font=('Arial', 20, 'normal'))


    def increase(self):
        self.clear()
        self.score= self.score+1
        self.write(f" score= {self.score}", align="Center", font=('Arial', 20, 'normal'))