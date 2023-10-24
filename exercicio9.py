import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(5)
colors = ['purple', 'blue' , 'green' , 'pink' , 'grey' , 'red' , 'yellow' , 'brown' , 'orange' , 'white']

for c in range(360):
    turtle.color(random.choice(colors))
    turtle.forward(2)
    turtle.right(1)
