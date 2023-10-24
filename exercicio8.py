import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(3)

colors = ['purple', 'blue', 'yellow', 'green', 'pink' , 'red' , 'gray' , 'orange']
for _ in range (15):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(24)
