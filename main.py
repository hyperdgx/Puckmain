from ast import Lt
from operator import lt
import turtle
s = turtle.Screen()
turtle.speed(5)
turtle.hideturtle()
turtle.color("white")
turtle.bgcolor("black")
turtle.pensize(10)



def myPosition(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def hand():
    
    myPosition(-100,50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.circle(-20, 180)
    turtle.fd(100)
    turtle.bk(200)
    turtle.circle(20, -180)
    turtle.bk(200)
    turtle.fd(100)
    turtle.circle(-20, 180)
    turtle.fd(100)
    turtle.bk(80)
    turtle.circle(20, -180)
    turtle.bk(80)

def thum():
    myPosition(-100,50)
    turtle.circle(10, -35)
    turtle.lt(90)
    turtle.forward(32)
    turtle.circle(-10, 100)
    turtle.fd(40)
    turtle.lt(46)
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(30,30)
    turtle.forward(60)
    turtle.circle(20,70)
    turtle.fd(50)
    turtle.circle(100,30)
    turtle.fd(50)
    turtle.circle(-100,30)
    turtle.penup()
    turtle.right(-78)
    turtle.fd(120)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(-90,30)
    turtle.fd(52)
    turtle.circle(20,44)
    turtle.fd(60)

hand()
thum()

    


turtle.done()
