from turtle import Turtle

class Snake:
    def __init__(self):
        self.turtles = []
        self.positions = [(-40, 0), (-20, 0), (0, 0)]
        self.createSnake()
        self.head = self.turtles[-1]
    def createSnake(self):
        for i in range(len(self.positions)):
            newTurtle = Turtle("square")
            newTurtle.penup()
            newTurtle.color("white")
            newTurtle.goto(self.positions[i])
            self.turtles.append(newTurtle)
    def move(self):
        for i in range(len(self.turtles) - 1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.forward(20)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_segment)

    def up(self):
        if (self.head.heading() != 270):
            self.head.setheading(90)
    def down(self):
        if (self.head.heading() != 90):
            self.head.setheading(270)
    def right(self):
        if (self.head.heading() != 180):
            self.head.setheading(0)
    def left(self):
        if (self.head.heading() != 0):
            self.head.setheading(180)

