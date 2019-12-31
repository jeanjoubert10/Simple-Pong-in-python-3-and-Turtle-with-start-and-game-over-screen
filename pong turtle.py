# Simple Pong game using Python 3 and Turtle module J Joubert 21 Oct 2019
# Sound only for mac using afplay
# winsound for windows
#     import windsound
#     winsound.PlaySound('filename.wav, winsound.SND_ASYNC')
# linux uses aplay

# You can drag paddle 1 (p1) with the mouse


import turtle
import random
import os
#import time # and time.sleep(0.017) windows?

score_a = 0
score_b = 0

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.title('Simple Pong with Python3 and Turtle')
wn.tracer(0)

p1 = turtle.Turtle()
p1.shape('square')
p1.color('white')
p1.shapesize(5,1) # Turtle still facing right (x axis is first - stretch_wid)
# Can also p1.shapesize(stretch_wid=5, stretch_len=1)
# Now 20x100 pixels
p1.up()
p1.goto(-350,0)

p2 = turtle.Turtle()
p2.shape('square')
p2.color('white')
p2.shapesize(5,1)
p2.up()
p2.goto(350,0)

# Turtle is 20x20 pixels
ball = turtle.Turtle()
ball.shape('circle')
ball.color('blue')
ball.up() # Pen up - you do not want to draw with the ball
ball.dx = random.choice((-5, 5)) # Movement in x (may need change in windows eg 0.03)
ball.dy = random.choice((-5, 5))

# Pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0   PlayerB: 0", align="center", font=("Courier", 24, "normal"))


def border_check():
    if ball.ycor()>290 or ball.ycor()<-290: 
        ball.dy *= -1 # Switch between positive/negative direction


def p1_up():
    if p1.ycor() <= 250:  # If paddle is below the top (y = 250) - move up 40 pixels
        p1.sety(p1.ycor()+40)

        
def p1_down():
    if p1.ycor() >= -250:
        p1.sety(p1.ycor()-40)


def p2_up():
    if p2.ycor() <= 250:
        p2.sety(p2.ycor()+40)


def p2_down():
    if p2.ycor() >= -250:
        p2.sety(p2.ycor()-40)

wn.listen()
wn.onkeypress(p1_up, "w")
wn.onkeypress(p1_down, 's')
wn.onkeypress(p2_up, 'Up')
wn.onkeypress(p2_down, 'Down')

game_over = False


while not game_over:
    wn.update()
    #time.sleep(0.017) # windows?
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    border_check()

    if ball.xcor() > 390: # Score player A - ball out on the right
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}   PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system('say "Score"')


    if ball.xcor() < -390: # Score player B - ball out on the left
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {}   PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system('say "Score"')
        
    # Paddle and ball collisions
    
    # For the right side fist
    # paddle x is at 350 but is 20 pixels wide (left side at 340 and right side 360)
    # ball x + 10 pixels = right side of ball
    # ball y + 10 = top must be above paddle bottom (paddle y-50) - y was stretched from 20 to 100 pixels
    # ball y - 10 = bottom must be below paddle top (paddle y+50)
    
    if (ball.xcor()+10 >= 340) and (ball.xcor()+10 <= 350) and ball.dx > 0 :
        if (ball.ycor()-10 <= p2.ycor() + 50) and (ball.ycor()+10 >= p2.ycor()-50):
            ball.dx *= -1

    # For the left or minus side
    if (ball.xcor()-10 <= p1.xcor()+10) and (ball.xcor()-10 >= p1.xcor()) and ball.dx < 0:
        if (ball.ycor() <= p1.ycor() + 60) and (ball.ycor() >= p1.ycor() -60):
            ball.dx *= -1

    # Stop if player reaches 10
    if score_a == 10 or score_b == 10:
        game_over = True


    # You can drag p1 with the mouse with this simple command!!
    p1.ondrag(p1.goto)




    



