from turtle import Turtle ,Screen
from snake import Snake
from food import Food
from scoreboard import Score
s=Screen()
import time
s.setup(width=400,height=400)
s.title("SNAKE GAME")
s.bgcolor("black")
s.tracer(0)

sn= Snake()
f=Food()
sc=Score()

s.listen()
s.onkey(sn.up,"Up")
s.onkey(sn.down,"Down")
s.onkey(sn.left,"Left")
s.onkey(sn.right,"Right")
ssc = sc.score
game=True
while game :
  s.update()

  time.sleep(0.1)

  sn.move()

  if sn.segments[0].distance(f)<15:
     sc.increase()
     sn.extend()
     f.refresh()
  if sn.segments[0].xcor()>180 or sn.segments[0].xcor() <-180 or sn.segments[0].ycor() < -180 or sn.segments[0].ycor() > 180 :
      print("u hit the wall")
      game=False
      sc.game_over()
      break

  for segment in  sn.segments :
    if segment== sn.segments[0]:
        pass
    elif sn.segments[0].distance(segment) < 10 :
        game=False
        print("u hit urself")
        sc.game_over()

s.exitonclick()




