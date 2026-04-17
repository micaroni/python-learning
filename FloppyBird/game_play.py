from turtle import Screen, Turtle
from random import randint
from flappybird import Bird

MOVE_SPEED = 10
MOUNTAIN_START = (400, -83)


class Ground(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=15, stretch_len=800)
        self.penup()
        self.goto(0, -280)


class Cloud:
    def __init__(self):
        self.all_clouds = []
        self.cloud_speed = MOVE_SPEED

    def create_cloud(self):
        random_chance = randint(1, 40)

        if random_chance == 1:
            if self.all_clouds:
                new_cloud = self.all_clouds[-1].clone()
            else:
                new_cloud = Turtle('circle')
                new_cloud.color('white')
                new_cloud.penup()

            new_cloud.shapesize(stretch_wid=randint(1, 4), stretch_len=randint(4, 7))
            random_y = randint(-70, 175)
            new_cloud.goto(400, random_y)

            self.all_clouds.append(new_cloud)

    def move_clouds(self):
        for clOud in self.all_clouds:
            clOud.backward(self.cloud_speed)


class Mountain:
    def __init__(self):
        self.all_mountains = []
        self.mountain_speed = MOVE_SPEED

    def create_mountain(self):
        random_chance = randint(1, 40)

        if random_chance == 1:
            if self.all_mountains:
                new_mountain = self.all_mountains[-1].clone()
            else:
                new_mountain = Turtle('triangle')
                new_mountain.color('tan')
                new_mountain.penup()
                new_mountain.tilt(90)

            new_mountain.shapesize(stretch_wid=5, stretch_len=8)
            new_mountain.goto(MOUNTAIN_START)

            self.all_mountains.append(new_mountain)

    def move_mountains(self):
        for mOuntain in self.all_mountains:
            mOuntain.backward(self.mountain_speed)


game_on = True


def collision():
    global game_on
    #detect collision with cloud
    for clOud in cloud.all_clouds:
        if clOud.distance(birdy) < 40:
            game_on = False

    # detect collision with mountain
    for mOuntain in mountain.all_mountains:
        if mOuntain.distance(birdy) < 40:
            game_on = False

    #detect collision with ground
    if birdy.ycor() < -275:
        game_on = False


def run():
    if game_on:
        mountain.create_mountain()
        mountain.move_mountains()

        cloud.create_cloud()
        cloud.move_clouds()

        collision()

        screen.update()
        screen.ontimer(run, 100)


screen = Screen()
screen.setup(800, 400)
screen.bgcolor('light blue')
screen.title("FloppyBird")
screen.tracer(0)

mountain = Mountain()
cloud = Cloud()
ground = Ground()
birdy = Bird()

screen.listen()
screen.onkey(birdy.go_up, "Up")
screen.onkey(birdy.go_down, "Down")

run()

screen.mainloop()
screen.exitonclick()
