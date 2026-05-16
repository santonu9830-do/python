import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("lightgreen")
my_wn.title("Turtle")
my_turtle = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_turtle.forward(size + 1)
        my_turtle.left(90)
    size += 1
    size -= 5       
turtle.done()