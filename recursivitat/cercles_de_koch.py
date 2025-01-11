import turtle
import yogi

def koch(n: int, d: int):
    if n == 0:
        return
    turtle.circle(d)
    turtle.right(180)

    for _ in range(4):
        koch(n - 1, d / 2)
        turtle.up()
        turtle.forward(d)
        turtle.right(90)
        turtle.forward(d)
        turtle.down()

    turtle.right(180)

n, d = yogi.read(int), yogi.read(int)

turtle.hideturtle()
turtle.speed(0)

koch(n, d)

turtle.done()