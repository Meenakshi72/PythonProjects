import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range (100):
    for colours in ["white","red"]:
        turtle.color(colours)
        turtle.circle(70)
        turtle.left(10)

turtle.hidetuetle()
