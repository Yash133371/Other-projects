import turtle
screen = turtle.Screen()
screen.title("Spiral")
screen.bgcolor("#000000")
screen.setup(800, 700)

t = turtle.Turtle()
t.speed(0)
t.pensize(10)
t.color("#00ff00")

for i in range(1, 100):
    t.forward(i)
    t.left(15)

turtle.done()