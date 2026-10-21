from turtle import Turtle,Screen

#Create the paddle
class Paddle(Turtle):
    def __init__(self,startingPosition):
        super().__init__()
        self.shape="square"
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)

        self.setpos(startingPosition)

    #Move the paddle up
    def moveUp(self):
        y_change = self.ycor() + 20
        self.goto(self.xcor(),y_change)

    #Move the paddle down
    def moveDown(self):
        y_change = self.ycor() - 20
        self.goto(self.xcor(),y_change)





