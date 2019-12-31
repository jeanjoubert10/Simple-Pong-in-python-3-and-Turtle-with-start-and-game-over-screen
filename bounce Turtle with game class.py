# Written in osX and IDLE
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
#import time # and time.sleep(0.017) windows?


class Ball(turtle.Turtle):
    def __init__(self, paddle):
        super().__init__(shape = 'circle')
        self.color('red')
        self.dx, self.dy = 6, 4
        self.up()
        self.paddle = paddle

             
    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)
        if self.xcor()<-230 or self.xcor()>230:
            self.dx *= -1
        if self.ycor()<-320 or self.ycor()>280:
            self.dy *= -1


    def bounce(self):
        if self.xcor()+10>= self.paddle.xcor()-50 and self.xcor()-10 <= self.paddle.xcor()+50 and self.dy<0:
            if self.ycor()-10 <= self.paddle.ycor()+10 and self.ycor()-10 >= self.paddle.ycor():
                self.dy *= -1
        

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__(shape = 'square')
        self.color('blue')
        self.up()
        self.goto(0,-200)
        self.shapesize(1,5)


    def right(self):
        if self.xcor()<220:
            self.goto(self.xcor()+40, self.ycor())

                  
    def left(self):
        if self.xcor()>=-220:
            self.goto(self.xcor()-40, self.ycor())


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.hideturtle()
        self.color('red')
        self.goto(0,0)

        
class Game():
    def __init__(self):
        self.win = turtle.Screen()
        self.win.setup(500,600)
        self.win.bgcolor('white')
        self.win.tracer(0)
        self.win.listen()
        self.running = True
        self.pen = Scoreboard()
        
    def new(self):
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.pen.clear()
        

        self.run()


    def run(self):
        self.playing = True
        
        while self.playing:
            self.events()
            self.update()


    def events(self):
        self.win.onkey(self.paddle.right, 'Right')
        self.win.onkey(self.paddle.left, 'Left')


    def update(self):
        
        self.win.update()
        #time.sleep(0.017) #windows?
        
        self.ball.move()
        self.ball.bounce()

        # Game over:
        if self.ball.ycor()<-280:
            self.playing = False
            self.ball.goto(1000,1000) # Hiding off screen
            self.paddle.goto(1000,1000)
            self.win.update()


    def show_start_screen(self):
        self.waiting = True
        self.win.onkey(self.wait_for_keypress, 'space')

        while self.waiting:
            self.pen.write('Press space to start new game', align='center', font=('Courier', 24, 'normal'))


    def show_game_over_screen(self):
        self.waiting = True
        while self.waiting:
            self.pen.write('Press space to start new game', align='center', font=('Courier', 24, 'normal'))


    def wait_for_keypress(self):
        self.waiting = False
        

     
game = Game()
game.show_start_screen()


while game.running:
    game.new()
    game.show_game_over_screen()




    
