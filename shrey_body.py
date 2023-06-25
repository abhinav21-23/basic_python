import turtle
def draw_body1():
    window=turtle.Screen()
    window.bgcolor("white")
    draw_shrey()
    window.exitonclick()

def draw_shrey():
    shrey=turtle.Turtle()
    shrey.shape("turtle")
    shrey.color("red")
    draw_head(shrey)
    draw_body(shrey)
    draw_arm(shrey)
    draw_leg1(shrey)
    draw_leg2(shrey)

def draw_head(shrey):
    shrey.circle(60)
    shrey.speed(3)
    shrey.right(60)

def draw_body(shrey):
    num=0
    while num<3:
        shrey.forward(150)
        shrey.right(120)
        shrey.speed(1)
        num+=1

def draw_arm(shrey):
    shrey.forward(60)
    shrey.left(60)
    shrey.forward(60)
    shrey.backward(60)
    shrey.right(60)
    shrey.backward(60)
    shrey.right(60)
    shrey.forward(60)
    shrey.right(60)
    shrey.forward(60)
    shrey.backward(60)
    shrey.left(60)
    shrey.forward(60)

def draw_leg1(shrey):
    shrey.left(120)
    shrey.forward(40)
    shrey.right(120)
    shrey.forward(120)

def draw_leg2(shrey):
    shrey.right(180)
    shrey.forward(120)
    shrey.right(60)
    shrey.forward(70)
    shrey.right(60)
    shrey.forward(120)
    draw_foot2(shrey)

def draw_foot1(shrey):
    shrey.color("blue")
    num=0
    while num<4:
        shrey.forward(20)
        shrey.left(90)
        num+=1

def draw_foot2(shrey):
    shrey.color("blue")
    num=0
    while num<4:
        shrey.forward(20)
        shrey.left(90)
        num+=1

draw_body1()
