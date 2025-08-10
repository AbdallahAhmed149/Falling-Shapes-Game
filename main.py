from turtle import Screen
from bowl import Bowl
from score import Score_board
from shapes import Shapes
import time

window = Screen()
window.setup(width=1000, height=800)
window.title("Falling Shapes Game")
window.bgcolor("black")
window.tracer(0)

bowl = Bowl()
board = Score_board()
score = 0
board.write(f"Score: {score}", font=("Arial", 25, "bold"), align="center")

window.listen()
window.onkey(bowl.move_right, "Right")
window.onkey(bowl.move_left, "Left")

game_on = True

while game_on:
    window.update()
    shape = Shapes()
    while -450 < shape.ycor() <= 500:
        window.update()
        time.sleep(0.025)
        shape.move_shapes()

        if (
            shape.shape() == "square"
            and shape.distance(bowl) < 50
            and shape.ycor() <= -340
        ):
            shape.hideturtle()
            score += 2

            if score >= 50:
                game_on = False
                shape.hideturtle()
                window.update()
                board.clear()
                board.goto(0, 0)
                board.write(
                    f"YOU WON! 🎉",
                    font=("Arial", 25, "italic"),
                    align="center",
                )
                break

            else:
                shape = Shapes()
                board.clear()
                board.write(
                    f"Score: {score}", font=("Arial", 25, "bold"), align="center"
                )

        elif (
            shape.shape() == "circle"
            and shape.distance(bowl) < 50
            and shape.ycor() <= -340
        ):
            shape.hideturtle()
            score += 1

            if score >= 50:
                game_on = False
                shape.hideturtle()
                window.update()
                board.clear()
                board.goto(0, 0)
                board.write(
                    f"YOU WON! 🎉",
                    font=("Arial", 25, "italic"),
                    align="center",
                )
                break

            else:
                shape = Shapes()
                board.clear()
                board.write(
                    f"Score: {score}", font=("Arial", 25, "bold"), align="center"
                )

        elif (
            shape.shape() == "turtle"
            and shape.color()[0] != "white"
            and shape.distance(bowl) < 50
            and shape.ycor() <= -340
        ):
            shape.hideturtle()
            score += 5

            if score >= 50:
                game_on = False
                shape.hideturtle()
                window.update()
                board.clear()
                board.goto(0, 0)
                board.write(
                    f"YOU WON! 🎉",
                    font=("Arial", 25, "italic"),
                    align="center",
                )
                break

            else:
                shape = Shapes()
                board.clear()
                board.write(
                    f"Score: {score}", font=("Arial", 25, "bold"), align="center"
                )

        elif (
            shape.shape() == "triangle"
            and shape.distance(bowl) < 50
            and shape.ycor() <= -340
        ):
            shape.hideturtle()
            shape = Shapes()
            score = 0
            board.clear()
            board.write(f"Score: {score}", font=("Arial", 25, "bold"), align="center")

        elif (
            shape.shape() == "turtle"
            and shape.color()[0] == "white"
            and shape.distance(bowl) < 50
            and shape.ycor() <= -340
        ):
            game_on = False
            shape.hideturtle()
            board.clear()
            board.goto(0, 0)
            board.write(
                f"GMAE OVER! ☠\nYour Score: {score}",
                font=("Arial", 25, "italic"),
                align="center",
            )


window.exitonclick()
