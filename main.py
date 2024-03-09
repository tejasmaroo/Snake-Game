from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
    
'''{segment1 = Turtle("square")
segment1.color("white")

segment2 = Turtle("square")
segment2.color("white")
segment2.goto(-20, 0)

segment3 = Turtle("square")
segment3.color("white")
segment3.goto(-40, 0)
}

{starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for positions in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)
}
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    {for seg in segments:
        seg.forward(20)}

    {for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)}'''

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")


def start_game():
    if True:

        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.065)

            snake.move_snake()

            # Detect collision with the food.
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                score.increase_score()

            # detect collision with wall
            if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
                score.reset()
                snake.reset()

            # detect collision with tail
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    score.reset()
                    snake.reset()


screen.onkey(start_game, "e")
screen.exitonclick()

