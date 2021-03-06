#Import An Image In Your Game
#CodeWithNick
#Python -- TurtleGraphics 

import turtle


#Register The Shape
turtle.register_shape("...")
turtle.register_shape("...")

#Set The Screen
wn = turtle.Screen()
wn.title("Animation")
wn.bgcolor("pink")
wn.update()


#Make The Player
player = turtle.Turtle()
player.penup()
player.shape("...")


#Functions
def left():
    player.speed(0)
    player.shape("...")
    player.setheading(180)
    player.fd(100)
def right():
    player.speed(0)
    player.shape("...")
    player.setheading(0)
    player.fd(100)


turtle.listen()
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

