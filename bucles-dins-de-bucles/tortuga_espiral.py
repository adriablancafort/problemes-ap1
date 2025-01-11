import yogi
import turtle

n = yogi.read(int)
m = yogi.read(int)

for i in range(0, n + 1):
    turtle.back(m*i)
    turtle.left(90)
    turtle.back(m*i)
    turtle.left(90)

turtle.done()