import turtle
import math

def drawCircle(x, y, radius):
    t = turtle.Turtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.circle(radius)



def main():
    x = 25
    y = 75
    radius = 75
    drawCircle(x, y, radius)

main()