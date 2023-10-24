
import turtle
turtle = turtle.Turtle()

for _ in [1, 2, 3]:
    turtle.shape('square')
    turtle.color('yellow')
    turtle.forward(80)
    turtle.right(120)

turtle.goto(120 , 0)
turtle.setheading(270)

for _ in [1, 2, 3, 4]:
  turtle.color('blue')
  turtle.shape('arrow')
  turtle.forward(160)
  turtle.right(90)
