# Very simple ball paddle game J Joubert 4 Nov 2019
# Writtten on mac osx - may need minor changes for windows as shown
# This code can be copied, changed, updated and if improved - please let me know how!!


import turtle
#import time # and time.sleep(0.017) windows?

win = turtle.Screen()
win.title('Paddle Game')
win.setup(500,600)
win.tracer(0) # Stops all animation until win.update() - try without this!!
win.listen() # Listen for key presses (right and left)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.up() # lift pen up - you do not want to draw

# Chosen ball speed in x and y axis
ball.dx = 5  # May need change in windows eg 0.05
ball.dy = 5

paddle = turtle.Turtle()
paddle.shape('square')
paddle.shapesize(1,5) # 5x on y axis (turtle still looking right)
paddle.color('blue')
paddle.up()
paddle.goto(0,-260)


def paddle_right(): # Move paddle 50 pixels right only if still in screen
    if paddle.xcor()<180:
        paddle.goto(paddle.xcor()+50, paddle.ycor())

def paddle_left():
    if paddle.xcor()>= -150:
        paddle.goto(paddle.xcor()-50, paddle.ycor())


win.onkey(paddle_right, 'Right')
win.onkey(paddle_left, 'Left')

def move_ball():
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    # Change dx if ball gets to either side
    if ball.xcor() >=230 or ball.xcor()<= -240:
        ball.dx *= -1

    # Change dy if ball gets to top
    if ball.ycor() >= 290:
        ball.dy *= -1

    # Reset ball to middle if out on the bottom
    if ball.ycor() <= -280:
        ball.goto(0,0)
        ball.dy *= -1


def ball_bounce(): # Bounce on paddle

    # If ball moving down and at level of paddle and between the left and right side, dy * -1
    if ball.dy<0 and ball.ycor()<=-245 and (paddle.xcor()-60 <= ball.xcor() <= paddle.xcor()+60):
        ball.dy *= -1

        
while True:
    win.update()
    move_ball()
    ball_bounce()
    #time.sleep(0.017) # windows?

    
