import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(5)

colors = ['purple', 'blue' , 'green' , 'pink' , 'grey']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(120)