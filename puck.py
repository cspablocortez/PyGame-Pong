from settings import *
from random import randint

class Puck:
    def __init__(self):
        self.color = (255, 255, 255)
        self.size = 15
        self.x = int(WIDTH / 2)
        self.y = int(HEIGHT / 2)
        self.x_vel = randint(2, 4)
        self.y_vel = randint(2, 4)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):

        if self.x < 0 or self.x > (WIDTH - self.size):
            sleep(0.5)
            self.color = (0, 0, 255)
            self.x = WIDTH / 2
            self.y = HEIGHT / 2
            self.x_vel = randint(-4, 4)
            self.y_vel = randint(-4, 4)
            self.color = (255, 255, 255)

        if self.y < 0 or self.y > (HEIGHT - self.size):
            self.y_vel *= -1

        self.x += self.x_vel
        self.y += self.y_vel
        self.rect = pygame.draw.rect(screen, self.color, [int(self.x), int(self.y), self.size, self.size], 0)

    def check_collision(self, sprite):
        if self.rect.colliderect(sprite):
            self.x_vel *= -1.1
            self.y_vel *= -1.1