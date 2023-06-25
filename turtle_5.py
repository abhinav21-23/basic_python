import turtle
colors=["red", "blue", "green", "yellow", "orange", "pink"]
a=turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    a.pencolor(colors[i%6])
    a.forward(i)
    a.left(59)
    a.width(i/100+1)
