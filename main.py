# Space Invaders game in Python 3.6 
# MONADICAL test

import turtle
import os
import math
import random
import winsound

#Setup screen
wn = turtle.Screen()
wn.bgcolor("black")
l = 320
wn.setworldcoordinates(-l,-l,l,l)
wn.title("Space Invaders v1.0")
wn.bgpic("images/nebulosa.gif")

# Register shapes
turtle.register_shape("images/player.gif")
turtle.register_shape("images/lazer.gif")
turtle.register_shape("images/invader.gif")

#Draw borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
  border_pen.fd(600)
  border_pen.lt(90)
border_pen.hideturtle()

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scoreString = "Score: %s" %score
score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Player turtle
playa = turtle.Turtle()
playa.color("blue")
playa.shape("images/player.gif")
playa.penup()
playa.speed(0)
playa.setposition(0, -260)
playa.setheading(90)

playaSpeed = 15

# Enemies list
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
  enemies.append(turtle.Turtle())

for enemy in enemies:
  enemy.color("Red")
  enemy.shape("images/invader.gif")
  enemy.penup()
  enemy.speed(0)
  x = random.randint(-200, 200)
  y = random.randint(100, 250)
  enemy.setposition(x, y)

enemySpeed = 2


# Bullet for aliens! okno
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("images/lazer.gif")
bullet.penup()
bullet.speed(0)
bullet.setposition(0, -400)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

bulletSpeed = 20

# Bullet states
# ready - ready to shoot
# fire - bullet is firing
bulletState = "ready"

#Moving playa left and right
def move_left():
  x = playa.xcor()
  x -= playaSpeed
  x = -280 if x < -280 else x
  playa.setx(x)

def move_right():
  x = playa.xcor()
  x += playaSpeed
  x = 280 if x > 280 else x
  playa.setx(x)

def fire_bullet():
  global bulletState
  
  if bulletState == "ready":
    # Play sound
    winsound.PlaySound("sounds/laser.wav", winsound.SND_ASYNC)
    # Update state
    bulletState = "fire"
    # Move bullet above player
    x = playa.xcor()
    y = playa.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()

def isCollision(t1, t2):
  dist = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
  return True if dist < 15 else False

#Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

#Main loop
while True:

  for enemy in enemies:
    # Move the enemy
    x = enemy.xcor()
    if x > 280 or x < -280:
      for e in enemies:
        e.sety(e.ycor() - 40)
      enemySpeed *= -1
    x += enemySpeed
    enemy.setx(x)

    # Check for collisions
    if isCollision(bullet, enemy):
      # Reset bullet
      bullet.hideturtle()
      bulletState = "ready"
      bullet.setposition(0, -400)
      # Reset enemy
      x = random.randint(-200, 200)
      y = random.randint(100, 250)
      enemy.setposition(x, y)
      # Update score
      score += 10
      scoreString = "Score: %s" %score
      score_pen.clear()
      score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
      # Play sound
      winsound.PlaySound("sounds/explosion.wav", winsound.SND_ASYNC)

    if isCollision(playa, enemy):
      playa.hideturtle()
      enemy.hideturtle()
      print("Game Over")
      break

  # Move the bullet
  if bulletState == "fire":
    y = bullet.ycor()
    y += bulletSpeed
    bullet.sety(y)

  # Check bullet top collision
  if bullet.ycor() > 275:
    bullet.hideturtle()
    bulletState = "ready"


# wn.mainloop()
# delay = input("Press ENTER to finish.")