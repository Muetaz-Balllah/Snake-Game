from turtle import Screen
from snake import Snake
from food import Food
from scoredboard import scoredboard
import time

window = Screen()
window.setup(600, 600)
window.bgcolor("black")
window.title("Sanke Game")
window.tracer(0)

mySnake = Snake()
food = Food()
score = scoredboard()

game_on = True
while game_on:
    mySnake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(mySnake.up, "Up")
    window.onkey(mySnake.down, "Down")
    window.onkey(mySnake.right, "Right")
    window.onkey(mySnake.left, "Left")
    if mySnake.head.distance(food) < 15:
        food.appear()
        mySnake.extend()
        score.increase_score()
    if mySnake.head.xcor() > 280 or mySnake.head.ycor() > 280 or mySnake.head.xcor() < -280 or mySnake.head.ycor() < -280:
        game_on = False
        score.game_over()
    for segment in mySnake.turtles[:-1]:
        if mySnake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

window.exitonclick()