import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(50)

turtle.backward(80)
turtle.right(90)

for _ in range(3):
  turtle.forward(50)
  turtle.left(90)