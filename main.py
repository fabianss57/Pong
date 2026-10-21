from turtle import Turtle,Screen
from paddle import Paddle

import time

#Create Screen to play Pong
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



#Create paddles for both players (Player 1 is on the left, Player 2 is on the right)
player1_paddle = Paddle((-350,0))
player2_paddle = Paddle((350,0))


#Have the screen listen for player keys; player 1 uses w and s, player 2 uses up and down arrow keys
screen.listen()
screen.onkey(player1_paddle.moveUp,"w")
screen.onkey(player1_paddle.moveDown,"s")

screen.onkey(player2_paddle.moveUp,"Up")
screen.onkey(player2_paddle.moveDown,"Down")


#Have the game run continuously
game_running = True
while game_running:
    screen.update()


screen.exitonclick()