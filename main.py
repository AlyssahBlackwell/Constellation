#print cancer constellation

import turtle
import time


t = turtle.Turtle()
t.color("black")
t.write("Alyssah Blackwell's Constellation project",align="center", font=("Verdana",15,"normal"))
window = turtle.Screen()
window.setup(width=1.0, height=1.0)
window.bgcolor("blue")
turtle.color("white")

time.sleep(5)
turtle.clear()
window.reset()

def pageone():
    window.bgpic("cancer.gif")
    window.update()


pageone()
time.sleep(5)
turtle.clear()
window.reset()

def pageTwo():
    turtle.dot(15)
    turtle.right(85)
    turtle.forward(80)
    turtle.dot(10)

    turtle.right(18)
    turtle.forward(40)

    turtle.dot(15)
    turtle.left(50)
    turtle.forward(80)
    turtle.dot(15)
    # now penup and go back to the previous dot and then pen down
    turtle.right(180)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()
    # now observe the direction of the turtle
    turtle.left(108)
    turtle.forward(50)
    turtle.dot(12)

    turtle.hideturtle()
    turtle.done()


pageTwo()
time.sleep(5)
turtle.clear()
window.reset()

def pagethree():
  window.bgpic("cancer.jpg")
  window.update()

pagethree()
time.sleep(5)
turtle.clear()
window.reset()

turtle.bye()
window.reset()




