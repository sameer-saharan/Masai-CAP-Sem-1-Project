from sketchpy import canvas
import turtle

obj = canvas.sketch_from_image("SKETCH/PHOTOS/irrfan.png")

t = turtle.Turtle()
t.speed(5)
t.penup()
t.pensize(10)
t.goto(180, -200)
t.pendown()
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)

obj.draw(threshold=110)
t.hideturtle()
turtle.done()