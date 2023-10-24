
import turtle

turtle = turtle.Turtle()

def pular(x , y):
    turtle.penup()
    turtle.goto(x , y)
    turtle.pendown()

for _ in range(4):
    turtle.shape('arrow')
    turtle.color('red')
    turtle.forward(100)
    turtle.right(90)
pular(-20 , 0)
turtle.setheading(90)
pular(-20 , 20)

for _ in range(4):
    turtle.shape('turtle')
    turtle.color('grey')
    turtle.forward(100)
    turtle.left(90)
turtle.setheading(0)
pular(0 , 20)

for _ in range(4):
    turtle.shape('triangle')
    turtle.color('blue')
    turtle.forward(100)
    turtle.left(90)
turtle.setheading(270)
pular(-20 , 0)

for _ in range(4):
   turtle.shape('circle')
   turtle.color('pink')
   turtle.forward(100)
   turtle.right(90)  
pular(-150 , -150)

for _ in range(4):
    turtle.shape('square')
    turtle.color('green')
    turtle.left(90)
    turtle.forward(280)
