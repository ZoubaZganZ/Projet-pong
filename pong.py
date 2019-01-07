import turtle 
import os

wn = turtle.Screen()
wn.title("Pong by Hugo Tesson")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0  )



 # Paddle B 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0  )

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white") 
ball.penup()
ball.goto(0, 0  )
ball.dx = 2
ball.dy = -2   

# Pen 
pen = turtle.Turtle
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_b_down():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

#Keyboard bind
wn.listen()
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True : 
	wn.update()

#Move the ball 
ball.sextx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)


# Border checking 
if ball.ycor() > 290:
	ball.stey(290)
	ball.dy *= -1

if ball.ycor() < -290:
	ball.stey(-290)
	ball.dy *= -1

if ball.xcor() > 390:
	ball.goto(0, 0)
	ball.dx *= -1

if ball.xcor() < -390:
	ball.goto(0, 0)
	ball.dx *= -1