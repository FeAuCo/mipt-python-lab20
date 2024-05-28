import pygame as pg
import random


# упражнение 1:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} - разность между концом и началом вектора по абсциссе.  {self.y} ' \
               f'- разность между концом и началом вектора по ординате.'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __neg__(self):
        return self.x * (-1), self.y * (-1)

    def value(self):
        return self.x, self.y


# упражнение 2: ???
# упражнение 3:
class Ball:
    def __init__(self, mass, coords, velocity, radius, color):
        self.mass = mass
        self.coords = coords
        self.velocity = velocity
        self.radius = radius
        self.color = color

    # def update(self, dt):
    #     return None
    # как???

    def render(self):
        pg.draw.circle(screen, self.color, (self.coords[0], self.coords[1]), self.radius)


pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption('Ball Game')
clock = pg.time.Clock()
running = True
created_balls = []
while running:
    dt = clock.tick(60) / 1000
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
            clicked_balls = [True if created_balls[i].coords[0] - created_balls[i].radius <=
                                    pg.mouse.get_pos()[0] <= created_balls[i].coords[0] + created_balls[i].radius
                                    and created_balls[i].coords[1] - created_balls[i].radius <=
                                    pg.mouse.get_pos()[1] <= created_balls[i].coords[1] + created_balls[i].radius
                             else False for i in range(len(created_balls))]
            if any(clicked_balls):
                # Упражнение 4:
                created_balls[clicked_balls.index(True)].color = (
                    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                created_balls[clicked_balls.index(True)].render()
                # Упражнение 5:
            else:
                created_balls.append(Ball(1, pg.mouse.get_pos(), 5, 30, (255, 255, 255)))
                created_balls[-1].render()
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
pg.quit()
