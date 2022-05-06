from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position, color):
        super().__init__()

        self.shape("square")
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), y=new_y)


      
        


