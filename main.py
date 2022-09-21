import turtle

#initial window setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#0D283D")
wn.setup(width=800, height=600)
wn.tracer(0)    #ensures manual updates for faster response

#main game loop
while True:
    wn.update()
