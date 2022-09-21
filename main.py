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

#ball
ball = turtle.Turtle()
ball.speed(0)   #defaults to max speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

#main game loop
while True:
    wn.update()
