from turtle import *
qelem = Turtle()
qelem.speed(0)
qelem.color("blue")
qelem.width(5)

qelem2 = turtle.Turtle()
qelem2.speed(0)
qelem2.circle(200)


def dordbucaq(kunc):
    for i in range(2):
        qelem.forward(kunc)
        qelem.left(90)


def ulduz(kunc):
    for i in range(5):
        qelem.forward(kunc)
        qelem.right(144)

ulduz(170)
done()