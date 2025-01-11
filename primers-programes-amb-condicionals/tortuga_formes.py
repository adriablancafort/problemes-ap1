import turtle
import yogi

f = yogi.read(str)

if f == "cercle":
    r = yogi.read(int)
    turtle.circle(r)
    turtle.done()

elif f == "quadrat":
    a = yogi.read(int)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.done()

elif f == "rectangle":
    a = yogi.read(int)
    b = yogi.read(int)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.done()

else:
    print("Forma no identificada")