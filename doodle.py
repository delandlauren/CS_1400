'''
Project name: Turtle Patterns 1
Author: Lauren DeLand
Due Date: 2022-02-19
Course: CS1400-005

Using the turtle funciton create a picture using turtle commands
'''

import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

''' FUNCTIONS '''
def drawMountains(peaks, mountain_height, tilt, penColor, fillColor):
    """Turtle draws a triangle and fills it in with a color for mountains"""
    t.pencolor(penColor)
    t.fillcolor(fillColor)
    t.begin_fill()
    for i in range(peaks):
        t.forward(mountain_height)
        t.lt(tilt)
    t.end_fill()
    
def drawGround(ground_height, ground_width, penColor, fillColor):
    """Turtle start pointing downwards in the lower left of the screen and draws the ground"""
    t.pencolor(penColor)
    t.fillcolor(fillColor)
    t.begin_fill()
    for i in range(2):
        t.forward(ground_height)
        t.rt(90)
        t.forward(ground_width)
        t.rt(90)
    t.end_fill()
    
def drawStem(stem_height, stem_width, tilt, penColor, fillColor):
    """ Start the turtle pointing down and then goes to the lower left half of the screen
        the turtle then draws two stems that are tall and 2 stems that are short in between
        the tall ones"""
    t.pencolor(penColor)
    t.fillcolor(fillColor)
    t.rt(tilt)
    t.begin_fill()
    for i in range(2):
        t.forward(stem_height)
        t.rt(90)
        t.forward(stem_width)
        t.rt(90)
    t.end_fill()
    
def drawFlower(petals, circumference, tilt, penColor, fillColor):
    """Turtle starts in the lower left of the screen and draws two blue flower
        and two red flower a inbetween the blue ones and lower"""
    t.pencolor(penColor)
    t.fillcolor(fillColor)
    t.speed(10)
    for i in range(petals):
        t.begin_fill()
        t.circle(circumference)
        t.rt(tilt)
        t.end_fill()
    
''' TEST FUNCTIONS '''
def testMountains():
    """ test mountain functions """
    t.up()
    t.goto(-600, -200)
    t.down()
    for i in range(4):
        drawMountains(3, 500, 120, "grey", "grey")
        t.up()
        t.seth(0)
        t.forward(250)
        t.down()
    t.up()
    t.goto(-425, -200)
    t.down()
    for i in range(4):
        drawMountains(3, 400, 120, "grey", "grey")
        t.up()
        t.seth(0)
        t.forward(250)
        t.down()
    
def testGround():
    """ Tests ground function """
    t.up()
    t.seth(270)
    t.goto(600, -200)
    t.down()
    drawGround(600, 1500, "black", "lightgreen")
    
def testStem():
    """ Tests stem fucntion """
    t.seth(270)
    t.up()
    t.goto(-300, -100)
    t.down()
    for i in range(2):
        drawStem(300, 20, 0, "black", "green")
        t.up()
        t.seth(0)
        t.forward(400)
        t.seth(270)
        t.down()
    t.up()
    t.goto(-100, -150)
    t.down()
    for i in range(2):
        drawStem(200, 20, 0, "black", "green")
        t.up()
        t.seth(0)
        t.forward(400)
        t.seth(270)
        t.down()

def testFlower():
    """ Test flower function """
    t.up()
    t.goto(-300, -100)
    t.down()
    for i in range (2):
        drawFlower(6, 40, 60, "black", "blue")
        t.up()
        t.seth(0)
        t.forward(400)
        t.down()
    t.up()
    t.goto(-100, -150)
    t.down()
    for i in range(2):
        drawFlower(6, 40, 60, "black", "red")
        t.up()
        t.seth(0)
        t.forward(400)
        t.down()
        
'''DRAWS THE PICTURE'''
turtle.bgcolor("skyblue")
testMountains()
testGround()
testStem()    
testFlower()
turtle.bye()