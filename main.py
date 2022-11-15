import turtle
import time
import random

delay = 0.1
score = 0
highScore = 0

#Creating the actual game window screen
window = turtle.Screen()
window.title = ("The Snake Game")
window.bgcolor("green yellow")

#adjusting width and heigh of window
window.setup(width = 600, height = 600)
window.tracer(0)

#creating the head of the snake
snakeHead = turtle.Turtle()
snakeHead.shape = ("square")
snakeHead.color("white")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "Stop"

#creating the food for the snake
snakeFood = turtle.Turtle()
colors = random.choice(['red', 'black', 'green'])
shapes = random.choice(['triangle', 'circle', 'square'])
snakeFood.speed(0)
snakeFood.shape(shapes)
snakeFood.color(colors)
snakeFood.penup()
snakeFood.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Current Score 0 & High Score: 0", align = "center",
          font = ("candara", 24, "bold"))

# now assigning the key directions from the user
def group():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"

def goDown():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"

def goLeft():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"

def goRight():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"

def move():
    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + 20)
    if snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)
    if snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)
    if snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)

window.listen()
window.onkeypress(group, "w")
window.onkeypress(goDown, "s")
window.onkeypress(goLeft, "a")
window.onkeypress(goRight, "d")

snakeSegments = []

while True:
    window.update()
    if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() < -290:
        time.sleep(1)
        snakeHead.goto(0,0)
        snakeHead.direction = "Stop"
        colors = random.choice(['red', 'black', 'green'])
        shapes = random.choice(['circle', 'square'])
        for segment in snakeSegments:
            segment.goto(1000,1000)
        snakeSegments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Current Score: {} High Score: {} ".format (
                  score, highScore), align = "center", font = ("candara", 24, "bold"))
        


