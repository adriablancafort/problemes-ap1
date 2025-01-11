import turtle

def pintar_abre(n: int, d: int, a: float) -> None:
    if n == 1:
        turtle.forward(d)
        turtle.back(d)
        return
    turtle.forward(d)
    turtle.right(a)
    pintar_abre(n - 1, d*3/4, a)
    turtle.left(2*a)
    pintar_abre(n - 1, d*3/4, a)
    turtle.right(a)
    turtle.back(d)

n = int(input())
d = int(input())
a = float(input())

turtle.left(90)

pintar_abre(n, d, a)

turtle.done()