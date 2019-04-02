#Turtle Graphics Game(Basic)
import turtle
import math
import random
import os

#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("bg.gif")
wn.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.color("gray")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
    side += 1
mypen.hideturtle()

#Title and Scoreboard
mypen.penup()
mypen.hideturtle()
mypen.setposition(-295,305)
scorestring = "Score: "
mypen.write(scorestring, False, align = 'left', font = ('Arial', 14, 'normal'))

title = turtle.Turtle()
title.color("yellow")
title.penup()
title.hideturtle()
title.setposition(-110,305)
title.write("KILL THE SPACE TURTLES!!!", False, align = 'left', font = ('Arial', 18, 'bold'))


#Create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)

#Create the score variable
score = 0

#Creat goals
maxGoals = 6
goals = []
colors = ['red','yellow','purple','green']

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color(colors[random.randint(0,3)])
    goals[count].shape('turtle')
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))

#Set speed variable
speed = 1

#Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    if speed != 1:
        speed -= 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False


#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

#Set player moving
while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor() > 299 or player.xcor() < -299:
        player.right(180)
        os.system("afplay jump.mp3&")
    if player.ycor() > 299 or player.ycor() < -299:
        player.right(180)
        os.system("afplay jump.mp3&")
    
    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(1)

        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
        
        #Collision checking
        if isCollision(player, goals[count]):
            goals[count].color(colors[random.randint(0,3)])
            goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            os.system("afplay bounce.mp3&")
            score += 1
            #Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-295,305)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align = 'left', font = ('Arial', 14, 'normal'))



delay = input("Press Enter to exit")