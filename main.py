import turtle

#initial window setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#0D283D")
wn.setup(width=800, height=600)
wn.tracer(0)    #ensures manual updates for faster response

#L Paddle
l_paddle = turtle.Turtle()
l_paddle.speed(0)   #defaults to max speed
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
    y += 20             #moves up by 20 pixels
    l_paddle.sety(y)    #stores new y coordinate

def l_paddle_down():
    y = l_paddle.ycor()
    y -= 20             #moves down by 20 pixels
    l_paddle.sety(y)    #stores new y coordinate

#User moves R paddle up/down
def r_paddle_up():
    y = r_paddle.ycor()
    y += 20             #moves up by 20 pixels
    r_paddle.sety(y)    #stores new y coordinate

def r_paddle_down():
    y = r_paddle.ycor()
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
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25


#main game loop
while True:
    wn.update()

    #moves ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checks if ball hits border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    #paddle/ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1