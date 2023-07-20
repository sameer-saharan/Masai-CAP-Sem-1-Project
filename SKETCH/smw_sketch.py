from sketchpy import canvas
import turtle

obj = canvas.sketch_from_image("SKETCH/PHOTOS/smw.png")

t = turtle.Turtle()
t.speed(5)
t.penup()
t.pensize(10)
t.goto(240, -260)
t.pendown()
t.left(90)
t.forward(480)
t.left(90)
t.forward(480)
t.left(90)
t.forward(480)
t.left(90)
t.forward(480)

obj.draw(threshold=150)
t.hideturtle()
turtle.done()