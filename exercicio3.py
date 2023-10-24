import turtle

turtle = turtle.Turtle()
turtle.shape('square')
turtle.pensize(10)

for repete in range(2):
    for color in ['black', 'pink' , 'blue' , 'red']:
        turtle.color(color)
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
    turtle.goto(0 , 200)    
    turtle.pendown() 