import turtle #Outside_In
import time
import random
print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    squares = int(num_str)
    angle = 180 - 180*(squares-2)/squares
    turtle.up
    x = 0
    y = 0
turtle.setpos(x, y)
turtle.done()