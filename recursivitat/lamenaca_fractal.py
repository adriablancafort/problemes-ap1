import turtle
import yogi

def amenaca(n: int, d: int):
    if n == 0:
        return
    if n == 1:
        for _ in range(3):
            turtle.forward(d)
            turtle.left(90)
        turtle.forward(d)
    else:
        for _ in range(3):
            turtle.forward(d)               
            amenaca(n - 1, d / 2)
        turtle.forward(d)

n, d = yogi.read(int), yogi.read(int)

turtle.speed(0)
turtle.hideturtle()

turtle.left(180)

amenaca(n, d)

turtle.done()