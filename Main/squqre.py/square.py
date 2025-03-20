import turtle

turtlescreen = turtle.Screen()
turtlescreen.bgcolor("red")
turtlescreen.setup(400,300)
turtlescreen.title('square')
turtleobj = turtle.Turtle()
for i in range(4):
    turtleobj.forward(100)
    turtleobj.right(90)
turtle.done()