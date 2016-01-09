import turtle
t = turtle.Pen()
def drawEightAngle(paint):
    if paint:
        t.begin_fill()
    for x in xrange(1,9):
        t.forward(30)
        t.right(45)
    if paint:
        t.end_fill()

drawEightAngle(True)
