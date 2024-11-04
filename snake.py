from turtle import Turtle

MOVE_DISTANCE = 20
positions = [0, -20, -40]


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.generate_snakes()

    def generate_snakes(self):
        for position in positions:
            self.add_segment(position, 0)

    def snake_movement(self):

        snake_length = len(self.snake_segments)

        for snake_index in range((snake_length - 1), 0, -1):
            new_x = self.snake_segments[snake_index - 1].xcor()
            new_y = self.snake_segments[snake_index - 1].ycor()
            self.snake_segments[snake_index].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)
        # self.snake_segments[0].forward(MOVE_DISTANCE)

    def move_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)
        # self.snake_segments[0].forward(MOVE_DISTANCE)

    def move_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)
        # self.snake_segments[0].forward(MOVE_DISTANCE)

    def move_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)
        # self.snake_segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, posx, posy):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.goto(posx, posy)
        self.snake_segments.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())

    def snake_reset(self):
        for segment in self.snake_segments:
            segment.hideturtle()
        self.snake_segments.clear()
        self.generate_snakes()
