from turtle import Turtle
start_position = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake():
    def __init__(self):
       self.segments =[]
       self.c_snake()


    def c_snake(self):
        for position in start_position:
          self.add_segment(position)

    def add_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
       for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
       self.segments[0].forward(15)


    def up(self):
        if self.segments[0].heading()!= DOWN:
         self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
         self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
         self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
         self.segments[0].setheading(LEFT)




