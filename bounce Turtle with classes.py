
# Very simple example of using Turtle with classes
# More or less the same as the Tkinter version in Python for Kids
# Written in osx and IDLE
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
#import time # and time.sleep(0.017) windows??


win = turtle.Screen()
win.setup(500,600)
win.bgcolor('black')
win.tracer(0)
win.listen()

class Ball(turtle.Turtle):
    def __init__(self, paddle):
        super().__init__(shape = 'circle')
        self.color('blue')
        self.dx, self.dy = 6, 4
        self.up()
        self.paddle = paddle
             
    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)
        if self.xcor()<-230 or self.xcor()>230:
            self.dx *= -1
        if self.ycor()<-280 or self.ycor()>280:
            self.dy *= -1

    def bounce(self):
        if self.xcor()+10>= self.paddle.xcor()-50 and self.xcor()-10 <= self.paddle.xcor()+50 and ball.dy<0:
            if self.ycor()-10 <= self.paddle.ycor()+10 and self.ycor()-10 >= self.paddle.ycor():
                self.dy *= -1
        

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__(shape = 'square')
        self.color('white')
        self.up()
        self.goto(0,-200)
        self.shapesize(1,5)

    def right(self):
        if self.xcor()<220:
            self.goto(self.xcor()+40, self.ycor())
                  
    def left(self):
        if self.xcor()>=-220:
            self.goto(self.xcor()-40, self.ycor())

       
paddle = Paddle()
ball = Ball(paddle)

win.onkey(paddle.right, 'Right')
win.onkey(paddle.left, 'Left')


while True:
    try:
        win.update()
        #time.sleep(0.017) # windows?
        
        ball.move()
        ball.bounce()
    except:
        print('Exit Game')
        break
