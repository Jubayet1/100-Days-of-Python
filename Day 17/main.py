from turtle import Turtle, Screen


tim = Turtle()

for num in range(3, 6):
    angle = 180 / num
    for number in num:
        tim.move(100)
        tim.left(angle)




screen = Screen()
screen.exitonclick()