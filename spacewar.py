#Spacewar by @coerres
import os
import random

#Import the Turtle
import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
        def __init__(self, spriteshape, color, startx, starty):
                turtle.Turtle.__init__(self, shape = spriteshape)
                self.speed(0)
                self.penup
                self.color(color)
                self.fd(0)
                self.goto(startx, starty)
                self.speed = 1

        def move(self):
                self.fd(self.speed)

class Player(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.speed = 4
            self.lives = 3
        
        def turn_left(self):
               self.lt(45)
        

#Create my sprites
player = Player("triangle", "white", 0, 0)

#Main game loop
while True:
      player.move()
      player.turn_left()
        







delay = input("Press enter to exit. > ")
