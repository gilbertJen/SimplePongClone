# Simple Pong Clone

import turtle
import random

"""
window properties 
window size in px
size is overridden on tiling window managers
tracer(0) removes auto refresh
"""
window = turtle.Screen()
window.title("Simple Pong Clone")
window.bgcolor("#272830")
window.setup(width=800, height=600)
window.tracer(0)

# Scores
score_1 = 0
score_2 = 0

"""
sprites:
left & right paddles, verticle bars
ball
"""

# left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("#CBCBCB")
paddle_left.penup()
paddle_left.goto(-350,0)

# right paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color("#CBCBCB")
paddle_right.penup()
paddle_right.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#CBCBCB")
ball.penup()
ball.goto(0,0)
ball.dx = .04
ball.dy = .04

# score
box = turtle.Turtle()
box.speed(0)
box.color("#CBCBCB")
box.penup()
box.hideturtle()
box.goto(0, 260)
box.write("Player 1: 0        Player 2: 0", align="center", font=("Minecraft", 24))

"""
functions:
paddle movements up & down
"""

# left paddle functions
def paddle_left_up():
	# update y coordinates
	y = paddle_left.ycor()
	y += 20
	paddle_left.sety(y)
	
def paddle_left_down():
	# update y coordinates
	y = paddle_left.ycor()
	y -= 20
	paddle_left.sety(y)

# right paddle functions
def paddle_right_up():
	# update y coordinates
	y = paddle_right.ycor()
	y += 20
	paddle_right.sety(y)
	
def paddle_right_down():
	# update y coordinates
	y = paddle_right.ycor()
	y -= 20
	paddle_right.sety(y)

# ball functions

	
# set keybindings	
window.listen()
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")	


# Main Game Loop
while True:
	window.update()
	
	# basic ball movement
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	"""
	check for border & reverse direction
	ball restarts with a random direction
	"""
	#top border
	if ball.ycor() > 290:
		ball.sety(290)
		a = random.randint(1,2)
		b = 1
		if a == 1:
			b = -1
		ball.dy *= b
		#ball.dy *= -1
		
	#bottom border
	if ball.ycor() < -290:
		ball.sety(-290)
		a = random.randint(1,2)
		b = 1
		if a == 1:
			b = -1
		ball.dy *= b
		#ball.dy *= -1
		
	#left border
	if ball.xcor() < -390:
		score_2 += 1
		box.clear()
		box.write("Player 1: {}        Player 2: {}".format(score_1, score_2), align="center", font=("Minecraft", 24))
		ball.goto(0,0)
		a = random.randint(1,2)
		b = 1
		if a == 1:
			b = -1
		ball.dx *= b
		
	#right border
	if ball.xcor() > 390:
		score_1 += 1
		box.clear()
		box.write("Player 1: {}        Player 2: {}".format(score_1, score_2), align="center", font=("Minecraft", 24))
		ball.goto(0,0)
		a = random.randint(1,2)
		b = 1
		if a == 1:
			b = -1
		ball.dx *= b

	"""
	Paddle and Ball Collision
	checks for intersection using x,y coordinates of paddle and ball
	"""
	
	# right paddle
	if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
	
	# left paddle
	if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
