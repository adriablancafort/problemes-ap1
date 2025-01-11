import yogi
import turtle

n = yogi.read(int)
m = yogi.read(int)

def quadrats(n, m):
    for i in range(1, n):
        for j in range(4):
            turtle.forward(m*i)
            turtle.left(90)

quadrats(n, m)
turtle.forward(m*n)
turtle.left(90)
turtle.forward(m*n)
turtle.left(90)
quadrats(n, m)
turtle.forward(m*n)
turtle.left(90)
turtle.forward(m*n)
turtle.left(90)
turtle.done()