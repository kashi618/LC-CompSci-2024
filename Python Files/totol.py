import turtle
pen = turtle.Turtle()

window = turtle.Screen()

pen.pensize(2)
pen.color("red")

angles = [0,90,60,90,90]

distances = [100,75,50,75,100]

pen.left(angles[0])
pen.forward(distances[0])
pen.left(angles[1])
pen.forward(distances[1])
pen.left(angles[2])
pen.forward(distances[2])
pen.left(angles[3])
pen.forward(distances[3])
pen.left(angles[4])
pen.forward(distances[4])

