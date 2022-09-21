import turtle
import winsound
import random

#initial window setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#0D283D")
wn.setup(width=800, height=600)
wn.tracer(0)    #ensures manual updates for faster response

#Scores for each player
score1 = 0
score2 = 0

#L Paddle
l_paddle = turtle.Turtle()
l_paddle.speed(10)   #defaults to max speed
l_paddle.shape("square")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.color("white")
l_paddle.penup()
l_paddle.goto(-350,0)

#R Paddle
r_paddle = turtle.Turtle()
r_paddle.speed(0)   #defaults to max speed
r_paddle.shape("square")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.color("white")
r_paddle.penup()
r_paddle.goto(350,0)

#User moves L paddle up/down
def l_paddle_up():
    y = l_paddle.ycor()
    if y < 245:
        y += 20             #moves up by 20 pixels
        l_paddle.sety(y)    #stores new y coordinate

def l_paddle_down():
    y = l_paddle.ycor()
    if y > -230:
        y -= 20             #moves down by 20 pixels
        l_paddle.sety(y)    #stores new y coordinate

#User moves R paddle up/down
def r_paddle_up():
    y = r_paddle.ycor()
    if y < 245:
        y += 20             #moves up by 20 pixels
        r_paddle.sety(y)    #stores new y coordinate

def r_paddle_down():
    y = r_paddle.ycor()
    if y > -230:
        y -= 20             #moves down by 20 pixels
        r_paddle.sety(y)    #stores new y coordinate

#keybindings
wn.listen()
wn.onkeypress(l_paddle_up, "w")
wn.onkeypress(l_paddle_down, "s")
wn.onkeypress(r_paddle_up, "Up")
wn.onkeypress(r_paddle_down, "Down")

#ball
ball = turtle.Turtle()
ball.speed(0)   #defaults to max speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))

#main game loop
while True:
    wn.update()

    #indicates starting direction of ball randomly
    if ball.xcor() == 0 and ball.ycor() == 0:
        firstDirection = random.randint(0,3)
        if firstDirection == 1:
            ball.dx *= -1
            ball.dy *= 1
        elif firstDirection == 2:
            ball.dx *= 1
            ball.dy *= -1
        elif firstDirection == 3:
            ball.dx *= -1
            ball.dy *= -1
    #moves ball        
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checks if ball hits top/bottom border
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    #checks if ball hits right/left border
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "bold"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "bold"))

    #paddle/ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() -40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() -40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1